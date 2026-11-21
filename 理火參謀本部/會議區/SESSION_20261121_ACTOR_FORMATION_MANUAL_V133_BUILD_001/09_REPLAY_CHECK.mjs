/**
 * AI-native CP1 static reference replay, based ONLY on 04_CANONICAL_EVENT_LOG.jsonl.
 * Not an independent ChatGPT conversation or host production MRC-001 reducer.
 * Usage: node 09_REPLAY_CHECK.mjs
 */
import { readFileSync } from "node:fs";
const events=readFileSync(new URL("./04_CANONICAL_EVENT_LOG.jsonl",import.meta.url),"utf8").trim().split("\n").map(JSON.parse);
const fails=[],check=(name,good)=>{console.log((good?"PASS ":"FAIL ")+name);if(!good)fails.push(name)};
const index=new Map(events.map((e,i)=>[e.event_id,i]));
const ofType=t=>events.filter(e=>e.event?.type===t);
const initial=ofType("INITIAL_MATERIAL_JUDGMENT"),reawake=ofType("MATERIAL_REWAKE_JUDGMENT");
const current=Object.fromEntries(initial.map(e=>[e.owner.id,{event_ref:e.event_id,standing:e.standing.state,receipt:e.receipt}]));
for(const x of reawake)current[x.owner.id]={event_ref:x.event_id,standing:x.standing.state,receipt:x.receipt};
const holds=ofType("SURVIVING_HOLDS_PRESERVED").flatMap(e=>e.unknown);
const end=ofType("SESSION_END");
const state={
 session_ref:events[0]?.session_ref,events:events.length,initial_seats:initial.map(e=>e.owner.id),
 current_stances:current,rewake_count:reawake.length,
 source_lock:ofType("P0_SOURCE_LOCK").map(e=>e.event_id),holds,
 current_manual:"V1.3",candidate_manual:"V1.3.3-CANDIDATE",
 human_checkpoint:ofType("HUMAN_DECISION_REQUEST").at(-1)?.standing.state,
 session_end:end.length?"ENDED":"NOT_RECORDED",
 weight_training:"NOT_TESTED",independent_pilot:"NOT_RUN"
};
check("01_unique_ids",index.size===events.length);
check("02_monotonic_sequence",events.every((e,i)=>e.sequence_no===i+1&&e.event_id==="EV-"+String(i+1).padStart(4,"0")));
check("03_same_session",events.every(e=>e.session_ref===state.session_ref));
check("04_required_CP1_fields",events.every(e=>e.event&&e.claim&&e.relation!==undefined&&e.premise&&e.source?.length&&e.owner?.id&&e.edge&&e.standing&&e.delta&&e.unknown&&e.authority&&e.receipt!==undefined&&e.materiality&&e.lineage));
check("05_materiality_on_every_event",events.every(e=>["MATERIAL","PROCEDURAL_OR_SOURCE"].includes(e.materiality?.standing)));
check("06_lineage_points_to_prior",events.every((e,i)=>(e.lineage?.prior_event_refs||[]).every(ref=>index.has(ref)&&index.get(ref)<i)));
check("07_five_rounds",["R1","R2","R3","R4","R5"].every(r=>events.some(e=>e.round_ref===r)));
check("08_CORE6_initial_complete",initial.length===6&&["N1","A","B","C","D","E"].every(x=>initial.some(e=>e.owner.id===x&&e.receipt)));
check("09_material_rewakes_owned_receipted",reawake.length===8&&reawake.every(e=>e.materiality.standing==="MATERIAL"&&e.owner.role==="CORE_SEAT"&&e.receipt));
check("10_latest_stances_preserve_QUIET",Object.keys(current).length===6&&["N1","A","B","C","D","E"].every(x=>current[x]?.event_ref));
check("11_unresolved_HOLD_retained",holds.includes("C_EMPIRICAL_HOLD")&&holds.includes("E_COST_UNKNOWN")&&holds.includes("D_REAL_BLIND_TEST_NOT_RUN"));
check("12_original_V10_L6_L7_not_erased",events.some(e=>e.event_id==="EV-0013"&&e.claim.text.includes("L6 Domain Method")&&e.claim.text.includes("L7 World Qualification")));
check("13_Track_A_not_Track_B",events.some(e=>e.event_id==="EV-0014"&&e.claim.text.includes("Track-A")&&e.claim.text.includes("Track-B"))&&state.weight_training==="NOT_TESTED");
check("14_first_lesson_spec_created",ofType("PUBLIC_LESSON_SPEC_ADMITTED").length===1);
check("15_sealed_access_gap_explicit",ofType("EVALUATOR_BANK_CANDIDATE_CREATED").some(e=>e.unknown.includes("HUMAN_ACCESS_CONTROL_REQUIRED")));
check("16_CURRENT_v13_not_promoted",state.current_manual==="V1.3"&&!events.some(e=>/CURRENT_PROMOTION|METHOD_ATLAS_PROMOTED|RUNTIME_UPDATED|PROTOCOL_CHANGED/.test(e.event.type)));
check("17_human_gate_without_session_end",state.human_checkpoint==="WAITING_HUMAN_DECISION"&&state.session_end==="NOT_RECORDED");
check("18_deterministic_replay",JSON.stringify(state)===JSON.stringify((()=>{
 const c=Object.fromEntries(initial.map(e=>[e.owner.id,{event_ref:e.event_id,standing:e.standing.state,receipt:e.receipt}]));
 for(const x of reawake)c[x.owner.id]={event_ref:x.event_id,standing:x.standing.state,receipt:x.receipt};
 return {...state,current_stances:c};})())));
console.log("RECONSTRUCTED_STATE="+JSON.stringify(state));
console.log("RESULT="+(18-fails.length)+"/18");
if(fails.length)process.exitCode=1;
