# Canonical Event — CORRECTIVE_REENTRY_REQUEST
**Event ID:** CR-EV-0001  
**Session:** SESSION_20261120_CLEAN_INTELLIGENCE_001_REENTRY_001  
**Parent case:** SESSION_20261120_CLEAN_INTELLIGENCE_001  
**Council Round:** R000 / Bootstrap (procedural only; no L8 required)  
**Origin:** HUMAN / AnjouRan, explicitly from current user turn  
**Semantic type:** CORRECTIVE_REENTRY_REQUEST  
**Adapter state:** ORIGIN_TYPE_ACCEPTED / NO_SEMANTIC_REWRITE  
**Target:** Original P1 unqualified candidate + open problem formation  
**Source:** current human instruction, Staff-HQ PATCH V0.1.1, original D0/D1 and reference material

```yaml
event_id: CR-EV-0001
event_type: CORRECTIVE_REENTRY_REQUEST
origin: {actor_type: HUMAN, actor_id: HUMAN_ANJOURAN_CURRENT_TURN}
new_human_constraints:
  city: "深圳市, 中國"
  capital_floor: NONE
  capital_ceiling: NONE
  business_question: "如何賺錢、有哪些成本、何時回收"
  desired_return: "one final .md file committed to GitHub"
  audit_priority: "full canonical event and round lineage in Git"
  round_count_constraint: NONE
reentry_only: true
expressly_not_authorized: [P1_APPROVAL,G0_30_DAY_EXECUTION,HKD_1_8M_APPROVAL,INCORPORATION,PROCUREMENT,SPENDING,EXTERNAL_CONTRACTS]
opening_routes:
  P1_CORRECTIVE: {status: CANDIDATE_FOR_REENTRY, qualified: false}
  OPEN_PROBLEM: {status: NO_PROPOSAL_YET, P0: NONE}
old_session_history_mutable: false
```

## Separate procedural qualification concern — CR-EV-0002
**Origin:** SECRETARY / factual source registration (not thesis).
**Type:** QUALIFICATION_GATE_CONFLICT_OPEN.
Training contract: FORMAL COUNCIL MAY RESUME ONLY IF LIHUO_PROJECT_QUALIFIED=TRUE. Current training status = FALSE. New human instruction authorizes corrective reentry but does not explicitly change training gate or provide 18-gate evaluation evidence. **Do not silently treat as formally qualified; allow scoped corrective reference workflow with terminal Council-qualification HOLD until lawfully resolved**. This distinction must survive executive reporting.

## Initial routing — CR-EV-0003
**Origin:** SECRETARY / deterministic source-appropriate routing only.
- P1 route material topics: target customer (N1/A), business model (A/B/E), source/right (A/B/C), architecture (B/D), sequencing/cost (D/E), legal qualification (C); all six potentially materially affected.
- Open problem route: D0/D1 + REFERENCE_SET + own seat contract, **do not provide P1 as privileged problem frame**; all six may form problem/question/new-path.
- No seat may be told that low-capex is preferred; no capital band is legitimate without cost recovery evidence.
- Initial two routes' outputs separately recorded, no Secretary combination.

**No substantive proposal selected at R000.**
