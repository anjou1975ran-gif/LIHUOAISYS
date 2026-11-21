import {readFileSync} from "node:fs";
import {replayCP1,renderHuman} from "./reference_replay.mjs";
const fixture=readFileSync(new URL("./fixture.jsonl",import.meta.url),"utf8").trim().split("\n").map(JSON.parse);
const state=replayCP1(fixture);
const view=renderHuman(state);
const negative=(events,pattern)=>{try {replayCP1(events);return false;} catch(e) {return String(e).includes(pattern);}};
const mutate=(eid,patch)=>fixture.map(e=>e.event_id===eid?{...e,...patch}:e);
const tests={
  T01_state_replay_idempotent:JSON.stringify(replayCP1(fixture))===JSON.stringify(state),
  T02_objection_survives:!!state.active_objections["OBJ-C-1"],
  T03_minority_hold_survives:state.minority_holds.length===1,
  T04_relation_responded_only_after_consumption:state.material_relations["REL-C-N1"].state==="RESPONDED",
  T05_human_gate_renders_request:view.kind==="DECISION_REQUEST"&&view.status==="WAITING_HUMAN_DECISION"&&!!view.question,
  T06_discard_human_view_no_effect:JSON.stringify(replayCP1(fixture))===JSON.stringify(state),
  T07_F_not_core:!state.stance_refs.F&&state.research_refs.includes("F-EXP001"),
  T08_unknown_survives:state.unknown_refs.includes("UNRESOLVED-CROSS-VERTICAL")&&state.unknown_refs.includes("UNRESOLVED-ECONOMIC-COST"),
  T09_forged_Secretary_stance_rejected:negative(mutate("EV-003",{origin:{actor_id:"SEC",role:"SECRETARIAT"}}),"NOT_SEAT_OWNED"),
  T10_missing_material_L8_rejected:negative(mutate("EV-004",{L8_evidence_ref:null}),"MATERIAL_CORE_JUDGMENT_WITHOUT_L8_REF"),
  T11_duplicate_event_rejected:negative([...fixture,fixture.at(-1)],"NONMONOTONIC_OR_DUPLICATE_EVENT"),
  T12_F_core_promotion_rejected:negative(fixture.map(e=>e.event_id==="EV-003"?{...e,origin:{actor_id:"F",role:"CORE_SEAT"},payload:{...e.payload,seat_ref:"F"}}:e),"F_NOT_CORE7"),
  T13_objection_cannot_become_auto_qualified:state.current_proposal?.standing==="CANDIDATE",
  T14_human_silence_not_approval:state.mandate.standing==="SECRETARY_INTERPRETATION_HUMAN_UNCONFIRMED"
};
const failures=Object.entries(tests).filter(([k,v])=>!v).map(([k])=>k);
for(const [name,result] of Object.entries(tests)) console.log((result?"PASS":"FAIL")+" "+name);
console.log("TOTAL "+(Object.keys(tests).length-failures.length)+"/"+Object.keys(tests).length);
if(failures.length) process.exitCode=1;
