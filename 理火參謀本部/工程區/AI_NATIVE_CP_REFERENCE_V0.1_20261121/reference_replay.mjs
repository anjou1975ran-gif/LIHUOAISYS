/**
 * CP1 → CP2 reference-only deterministic reducer.
 * NOT a formally qualified DAIL/IR implementation or independent/host runtime.
 * Input: ordered, already-qualified canonical events. Never infers materiality.
 */
export function replayCP1(events) {
  const state = {
    session_ref: null, mandate: null, current_proposal: null,
    stance_refs: {}, active_objections: {}, minority_holds: [],
    material_relations: {}, source_refs: [], research_refs: [],
    unknown_refs: [], human_gate: "NOT_REQUIRED",
    last_sequence: 0, event_ids: []
  };
  const seen = new Set();
  for (const e of events) {
    if (!e || typeof e !== "object" || !e.event_id || !Number.isInteger(e.sequence_no)) {
      throw Error("MALFORMED_EVENT");
    }
    if (seen.has(e.event_id) || e.sequence_no !== state.last_sequence + 1) {
      throw Error("NONMONOTONIC_OR_DUPLICATE_EVENT");
    }
    if (!e.origin || !e.origin.actor_id || !e.origin.role || !e.session_ref) {
      throw Error("MISSING_ORIGIN");
    }
    if (!Array.isArray(e.source_refs) || !e.source_refs.length) throw Error("MISSING_SOURCE");
    if (state.session_ref && e.session_ref !== state.session_ref) throw Error("MIXED_SESSION");
    const material = e.materiality?.standing === "MATERIAL";
    if (material && (!e.materiality?.owner_ref || !e.materiality?.basis_refs?.length)) {
      throw Error("MATERIALITY_WITHOUT_ORIGIN_BASIS");
    }
    if (material && e.origin.role === "CORE_SEAT" && !e.L8_evidence_ref) {
      throw Error("MATERIAL_CORE_JUDGMENT_WITHOUT_L8_REF");
    }
    if (e.origin.actor_id === "F" && e.origin.role === "CORE_SEAT") {
      throw Error("F_NOT_CORE7");
    }
    const a = e.origin.actor_id;
    const role = e.origin.role;
    const p = e.payload || {};
    switch (e.semantic_type) {
      case "MANDATE_RECORDED":
        if (role !== "SECRETARIAT" && role !== "HUMAN") throw Error("BAD_MANDATE_OWNER");
        state.mandate = {D0_ref:p.D0_ref, D1_ref:p.D1_ref, standing:p.standing};
        break;
      case "PROPOSAL_ADMITTED":
        if (!["HUMAN","CORE_SEAT","AUTHORIZED_OWNER"].includes(role)) throw Error("UNAUTHORIZED_PROPOSAL");
        state.current_proposal = {version_ref:p.version_ref, standing:"CANDIDATE"};
        break;
      case "STANCE_ORIGINATED":
      case "POSITION_RETAINED_WITH_REASON":
        if (role !== "CORE_SEAT" || a !== p.seat_ref) throw Error("NOT_SEAT_OWNED");
        if (e.semantic_type === "POSITION_RETAINED_WITH_REASON") {
          const r = state.material_relations[p.consumed_relation_ref];
          if (!r || r.target_seat_ref !== a || r.state !== "CONSUMED") {
            throw Error("RELATION_NOT_CONSUMED");
          }
          r.state = "RESPONDED";
        }
        state.stance_refs[a] = {stance_ref:p.stance_ref,proposal_version_ref:p.proposal_version_ref,standing:p.standing||"ACTIVE"};
        break;
      case "OBJECTION_ORIGINATED":
        if (role !== "CORE_SEAT" || a !== p.seat_ref) throw Error("OBJECTION_OWNER_INVALID");
        state.active_objections[p.objection_ref] = {
          origin:a,target_ref:p.target_ref,standing:"ACTIVE",
          source_refs:[...e.source_refs],premise_refs:[...(p.premise_refs||[])]
        };
        break;
      case "MINORITY_HOLD":
        if (role !== "CORE_SEAT" || a !== p.seat_ref) throw Error("HOLD_OWNER_INVALID");
        state.minority_holds.push({seat_ref:a,ref:p.hold_ref,objection_ref:p.objection_ref});
        break;
      case "MATERIAL_RELATION_DELIVERED":
        if (role !== "SECRETARIAT") throw Error("ROUTING_OWNER_INVALID");
        if (!state.active_objections[p.objection_ref]) throw Error("RELATION_MISSING_OBJECTION");
        state.material_relations[p.relation_ref] = {target_seat_ref:p.target_seat_ref,objection_ref:p.objection_ref,state:"DELIVERED"};
        break;
      case "MATERIAL_RELATION_CONSUMED": {
        if (role !== "CORE_SEAT") throw Error("CONSUMPTION_OWNER_INVALID");
        const r = state.material_relations[p.relation_ref];
        if (!r || r.target_seat_ref !== a || r.state !== "DELIVERED") throw Error("RELATION_NOT_DELIVERED");
        r.state = "CONSUMED";
        break;
      }
      case "RESEARCH_REFERENCE_ADMITTED":
        if (role !== "SECRETARIAT") throw Error("RESEARCH_REF_ADMISSION_OWNER");
        state.research_refs.push(p.source_ref);
        break;
      case "HUMAN_ACTION_REQUIRED":
        if (role !== "SECRETARIAT") throw Error("HUMAN_GATE_OWNER");
        if (!p.decision_question || !p.plain_language_context) throw Error("BAD_DECISION_REQUEST_SOURCE");
        state.human_gate = "REQUIRED";
        state.decision_request_source = {question:p.decision_question,context:p.plain_language_context,choices:p.choices||[]};
        break;
      default:
        throw Error("UNADMITTED_EVENT_TYPE:" + e.semantic_type);
    }
    state.session_ref = e.session_ref;
    state.last_sequence = e.sequence_no;
    state.event_ids.push(e.event_id);
    state.source_refs.push(...e.source_refs.filter(x => !state.source_refs.includes(x)));
    for (const x of e.unresolved_refs || []) {
      if (!state.unknown_refs.includes(x)) state.unknown_refs.push(x);
    }
    seen.add(e.event_id);
  }
  return state;
}
export function renderHuman(state) {
  if (state.human_gate === "REQUIRED") {
    if (!state.decision_request_source?.question) throw Error("WAITING_WITHOUT_DECISION_REQUEST");
    return {
      kind:"DECISION_REQUEST", status:"WAITING_HUMAN_DECISION",
      question:state.decision_request_source.question,
      context:state.decision_request_source.context,
      choices:state.decision_request_source.choices,
      surviving_objections:Object.keys(state.active_objections),
      minority_holds:state.minority_holds,
      unknowns:state.unknown_refs,
      event_refs:state.event_ids
    };
  }
  return {
    kind:"EXECUTIVE_BRIEF",
    current_proposal:state.current_proposal,
    objections:Object.keys(state.active_objections),
    minority_holds:state.minority_holds,
    unknowns:state.unknown_refs,
    event_refs:state.event_ids
  };
}
