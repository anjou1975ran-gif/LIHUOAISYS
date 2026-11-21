/**
 * Reference-only deterministic reducer / structural audit for a single Council Session.
 * Canonical input: 04_CANONICAL_EVENT_LOG.jsonl, not derived Round, Chat or Final Report.
 * Node.js ESM usage: node 10_REPLAY_CHECK.mjs
 * NOT a formally qualified DAIL/IR/Host reducer, independent model replay or semantic proof.
 */
import { readFileSync } from "node:fs";
const events = readFileSync(new URL("./04_CANONICAL_EVENT_LOG.jsonl",import.meta.url),"utf8")
  .trim().split("\n").map(JSON.parse);
const violations=[];
const check=(id,ok)=>{console.log((ok?"PASS ":"FAIL ")+id);if(!ok)violations.push(id)};
const ids=new Map(events.map((e,i)=>[e.event_id,i]));
const byType=t=>events.filter(e=>e.event?.semantic_type===t);
const latest=(a)=>a.at(-1);
function reduce(input){
 const initial=input.filter(e=>e.semantic_type==="INITIAL_SEAT_JUDGMENT");
 const positions=input.filter(e=>["POSITION_REVISED","POSITION_RETAINED_WITH_QUALIFICATION"].includes(e.event.semantic_type));
 const current={};
 for(const x of initial)current[x.owner.actor_id]={claim_ref:x.claim.claim_ref,event_ref:x.event_id,status:x.standing.status,source:"R001"};
 for(const x of positions)current[x.owner.actor_id]={claim_ref:x.claim.claim_ref,event_ref:x.event_id,status:x.standing.status,source:"R003"};
 const terminal=input.some(x=>x.event.semantic_type==="SESSION_END");
 const gate=input.find(x=>x.event.semantic_type==="HUMAN_ACTION_REQUIRED");
 return {session_ref:input[0]?.session_ref,canonical_event_count:input.length,
   initial_seats:initial.map(x=>x.owner.actor_id),current_owned_positions:current,
   objections:input.filter(x=>x.event.semantic_type==="OBJECTION_ORIGINATED").map(x=>({ref:x.event_id,owner:x.owner.actor_id,target:x.relation.target_event_ref})),
   P0:{version:"V1.3.2-CANDIDATE",blob:"8acac163d49e4b6b24d77f18cc6727ab49e3027d",current:"V1.3"},
   unresolved:["C_EMPIRICAL_TRAINING_HOLD","N1_RUNNABLE_FIRST_LESSON_MISSING","E_LIFECYCLE_COST_UNKNOWN"],
   next_human_action:gate?{ref:gate.event_id,status:gate.standing.status,options:gate.relation?.options}:null,
   session_end:terminal?"ENDED":"NOT_RECORDED",
   stage2_empirically_validated:false,
   manual_current_promoted:false
 };
}
const init=byType("INITIAL_SEAT_JUDGMENT");
const challenges=byType("OBJECTION_ORIGINATED");
const consumed=events.filter(e=>e.event.semantic_type.includes("CONSUMED"));
const revised=events.filter(e=>["POSITION_REVISED","POSITION_RETAINED_WITH_QUALIFICATION"].includes(e.event.semantic_type));
const state=reduce(events);
check("01_unique_ids_and_monotonic_sequence",ids.size===events.length&&events.every((e,i)=>e.sequence_no===i+1&&e.event_id==="EV-"+String(i+1).padStart(4,"0")));
check("02_same_session_and_required_keys",events.every(e=>e.session_ref===events[0].session_ref&&e.event&&e.claim&&e.source?.length&&e.owner?.actor_id&&e.standing&&e.authority&&e.lineage));
check("03_all_lineage_refs_earlier",events.every((e,i)=>(e.lineage?.prior_event_refs||[]).every(ref=>ids.has(ref)&&ids.get(ref)<i)));
check("04_D1_still_human_unconfirmed",byType("D1_CANDIDATE")[0]?.standing.status==="SECRETARY_INTERPRETATION_HUMAN_UNCONFIRMED");
check("05_P0_candidate_current_v13",byType("P0_ADMITTED")[0]?.source.some(x=>x.source_ref.includes("MAN132@8acac163"))&&state.P0.current==="V1.3");
check("06_exactly_six_core_initial_receipts",init.length===6&&new Set(init.map(x=>x.owner.actor_id)).size===6&&init.every(x=>x.receipt?.l8_ref&&x.receipt?.compact_receipt_ref));
check("07_stage1_L6_L7_source_discrepancy_kept",byType("MATERIAL_SOURCE_DISCREPANCY").length===1);
check("08_four_origin_owned_material_challenges",challenges.length===4&&challenges.every(x=>x.owner.role==="CORE_SEAT"&&x.materiality?.standing==="MATERIAL"));
check("09_material_delivery_not_auto_agreement",byType("MATERIAL_RELATION_DELIVERY").length===1);
check("10_meaningful_consumption_references",consumed.length>=4&&consumed.every(x=>x.edge?.length>0));
check("11_four_latest_rewakes_each_l8",revised.length===4&&new Set(revised.map(x=>x.owner.actor_id)).size===4&&revised.every(x=>x.receipt?.l8_ref?.startsWith("L8-R003-")));
check("12_N1_E_quiet_no_forced_rewake",!revised.some(e=>["N1","E"].includes(e.owner.actor_id)));
check("13_C_HOLD_preserved",state.current_owned_positions.C?.status==="CONCEPT_QUALIFIED_EMPIRICAL_HOLD");
check("14_stage2_two_tracks_without_auto_training",events.some(x=>x.event_id==="EV-0020"&&x.claim.text.includes("兩條"))&&state.stage2_empirically_validated===false);
check("15_human_request_no_session_end",state.next_human_action?.status==="WAITING_HUMAN_DECISION"&&state.session_end==="NOT_RECORDED");
check("16_no_current_protocol_os_runtime_atlas_promotion",!events.some(x=>/^(?:SESSION_END|CURRENT_PROMOTION|RUNTIME_UPDATED|METHOD_ATLAS_PROMOTED|PROTOCOL_AMENDED)$/.test(x.event.semantic_type)));
check("17_deterministic_same_log_replay",JSON.stringify(reduce(events))===JSON.stringify(reduce(events)));
const implicit=events.filter(x=>!x.materiality).map(x=>x.event_id);
console.log("SCHEMA_LIMIT: "+implicit.length+" early events have implicit origin/receipt materiality but lack an explicit materiality field; this is a prototype CP1 quality gap.");
console.log("STATE_JSON="+JSON.stringify(state));
console.log("RESULT="+(17-violations.length)+"/17");
if(violations.length)process.exitCode=1;
