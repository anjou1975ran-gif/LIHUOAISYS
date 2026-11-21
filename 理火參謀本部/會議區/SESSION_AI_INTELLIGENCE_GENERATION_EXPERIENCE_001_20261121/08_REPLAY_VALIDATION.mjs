/**
 * Node.js ESM. Deterministic reconstruction from CP1 Canonical Event Log only.
 * Usage: node 08_REPLAY_VALIDATION.mjs
 * Reads only 02_CANONICAL_EVENT_LOG.jsonl. Does not use Round/Chat/Final projections.
 * This is a session-specific reference reducer, not the deployed MRC-001 service.
 */
import { readFileSync } from "node:fs";

const path = new URL("./02_CANONICAL_EVENT_LOG.jsonl", import.meta.url);
const events = readFileSync(path, "utf8").trim().split("\n").map(JSON.parse);
const failures = [];
const check = (name, condition, detail = "") => {
  console.log((condition ? "PASS " : "FAIL ") + name + (detail ? " :: " + detail : ""));
  if (!condition) failures.push(name);
};
const ids = new Set(events.map(e => e.event_id));
const seqs = events.map(e => e.sequence_no);
const uniqueIds = ids.size === events.length;
const monotonic = seqs.every((n, i) => n === i + 1);
const sameSession = events.every(e => e.session_ref === events[0]?.session_ref);
const completeSchema = events.every(e =>
  e.schema_version && e.event_id && Number.isInteger(e.sequence_no) &&
  e.session_ref && e.round_ref && e.event && e.claim && e.source?.length &&
  e.owner?.actor_id && e.owner?.role && e.standing && e.delta &&
  Array.isArray(e.premise) && Array.isArray(e.edge) &&
  Array.isArray(e.unknown) && e.authority && Object.hasOwn(e, "relation") &&
  Object.hasOwn(e, "receipt")
);
const allPriorRefsResolve = events.every(e =>
  (e.lineage?.prior_event_refs || []).every(ref => ids.has(ref))
);
const byType = type => events.filter(e => e.event.event_type === type);
const initial = byType("INITIAL_PASS_JUDGMENT");
const rechecks = byType("STANCE_RECHECK");
const candidates = events.filter(e => e.event.event_type.startsWith("CANDIDATE_"));
const d1 = byType("D1_CANDIDATE_RECORDED")[0];
const p0 = byType("P0_NONE_RECORDED")[0];
const gate = byType("HUMAN_ACTION_REQUIRED")[0];
const keepOpen = byType("HUMAN_DECISION_KEEP_OPEN").at(-1);
const terminal = events.find(e => e.event.event_type === "SESSION_END");
const issues = byType("SURVIVING_ISSUES_RECORDED")[0];
const rounds = [...new Set(events.map(e => e.round_ref).filter(r => /^R[1-8]$/.test(r)))].sort();
const receiptLinked = initial.length === 6 && initial.every(e =>
  e.receipt?.l8_cycle_ref && e.receipt?.sger_ref && e.receipt?.compact_receipt_ref
);
const stanceOwners = rechecks.length === 6 && rechecks.every(e =>
  e.owner.actor_id !== "SEC" && e.lineage.prior_event_refs.length > 0
);
const noAutoApproval = d1?.standing?.status === "SECRETARY_INTERPRETATION_HUMAN_UNCONFIRMED" &&
  !events.some(e => /HUMAN_APPROVED|D1_CONFIRMED|SESSION_END/.test(e.event.event_type));
const noRuntimeChange = !events.some(e => /RUNTIME_CHANGE_AUTHORIZED|METHOD_ATLAS_PROMOTED|PROTOCOL_PATCH_ADMITTED/.test(e.event.event_type));
const state = {
  session_ref: events[0]?.session_ref,
  event_count: events.length,
  mandate: {type:"CONCEPT",standing:d1?.standing?.status || "MISSING"},
  proposal: p0 ? "NONE" : "UNKNOWN",
  round_coverage: rounds,
  initial_seat_judgments: Object.fromEntries(initial.map(e => [e.owner.actor_id, {
    claim_ref:e.claim.claim_id, receipt_ref:e.receipt?.sger_ref, standing:e.standing.status
  }])),
  current_seat_stances: Object.fromEntries(rechecks.map(e => [e.owner.actor_id, {
    claim_ref:e.claim.claim_id, standing:e.standing.status, change_basis:e.lineage.prior_event_refs
  }])),
  research_candidates: candidates.map(e => ({
    event_ref:e.event_id, owner:e.owner.actor_id, claim_ref:e.claim.claim_id, standing:e.standing.status
  })),
  surviving_unknowns: issues?.unknown || [],
  human_gate: gate ? {status:keepOpen ? "RESOLVED_KEEP_OPEN" : gate.standing.status, event_ref:gate.event_id, decision_event_ref:keepOpen?.event_id || null} : null,
  session_status: terminal ? "ENDED" : (keepOpen ? "OPEN_IDLE_BY_HUMAN_DECISION" : "AWAITING_HUMAN_DECISION"),
  session_end: terminal ? terminal.event_id : "NOT_RECORDED"
};
check("unique_event_ids", uniqueIds);
check("monotonic_sequence", monotonic);
check("single_session", sameSession);
check("required_typed_fields", completeSchema);
check("all_prior_event_refs_resolve", allPriorRefsResolve);
check("all_eight_rounds_present", rounds.length === 8 && rounds[0] === "R1" && rounds[7] === "R8");
check("six_initial_seat_receipts_linked", receiptLinked);
check("six_owned_stance_rechecks", stanceOwners);
check("four_candidates_retained", candidates.length === 4);
check("D1_unconfirmed_and_P0_none", noAutoApproval && p0?.standing?.status === "NONE_BY_DESIGN");
check("human_end_decision_reduced_without_terminal_event",
  !!gate && state.session_end === "NOT_RECORDED" &&
  (!keepOpen || (keepOpen.event_id === "EV-0041" && keepOpen.owner.actor_id === "HUMAN" &&
  state.human_gate.status === "RESOLVED_KEEP_OPEN" && state.session_status === "OPEN_IDLE_BY_HUMAN_DECISION")));
check("no_runtime_or_atlas_mutation", noRuntimeChange);
console.log("\nRECONSTRUCTED_STATE");
console.log(JSON.stringify(state, null, 2));
console.log("\nTOTAL " + (12 - failures.length) + "/12");
if (failures.length) process.exitCode = 1;
