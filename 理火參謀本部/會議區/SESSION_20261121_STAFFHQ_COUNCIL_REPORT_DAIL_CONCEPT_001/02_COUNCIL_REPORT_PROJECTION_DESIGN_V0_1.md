# Council Narrative Projection｜Research Concept Design V0.1
**Proposed working name:** `COUNCIL_NARRATIVE_PROJECTOR` / 參謀本部議事脈絡顯影
**Nature:** DAIL-first / CP3 derived human view / optional L9 callable research capability
**Not:** second Canonical Event Log, Council judge, L8 competitor, Main, Secretarial policy owner, official deployed tool.

## Why existing A–K Final Report is not enough
The formal A–K fields already cover Mandate, proposal evolution, findings, options, objections, stance, experts, engineering/cost, common sense, exit and human next action. Missing as a first-class **reader contract**: the **explanation of relationships between those facts**, especially:
- which competing questions caused a meaningful reframing;
- who objected to which specific claim, and on what evidence;
- whether the targeted owner actually consumed/responded/revised;
- why a new proposal version appeared, or why a minority remained;
- what was believed/qualified at the time versus what became known later;
- what would most change the outcome if found next;
- where the human can go to check each consequential statement.

## Three reader modes / one canonical history
**1. EXECUTIVE_BRIEF (default)** — five-to-eight short readable points: task, current phase, surviving paths, decisive unresolved issue, important objection, next human action if any. Existing six-question contract remains.
**2. NARRATIVE_FULL_REPORT (primary new value)** — a coherent story anchored to event graph, not dialogue theater. Proposed flexible sections:
  1. 會議要解決的原始問題與授權邊界；
  2. 開始時的主張／選項與人類需求；
  3. 關鍵交鋒：對象、反對根據、各方回應（沒回應要明寫）；
  4. 真正的轉折：哪些 material delta 使誰 KEEP/REVISE/WITHDRAW/BRANCH；保留 chronology vs explicit causal basis；
  5. 目前能成立什麼、尚無法成立什麼；
  6. 存活路線和最大成本／風險／異議；
  7. 下一個最有辨識力的證據或可行研究；
  8. 若人類行動不可替代，接現有 Decision Request，否則明記無需人類立即決定。
**3. AUDIT_EXPLAIN (on-demand)** — issue graph, claim lineage, event ID, source evidence, L8 trace references when actually present, unknown/authority limitations, unreviewed gaps. If a source is missing, report `EVIDENCE_GAP` rather than fill fiction.

Do not force eight headings into every report; these are coverage obligations, not a printed full-length checklist. E.g. no expert was summoned → one sentence or an expandable audit entry, not an invented expert chapter.

## Minimal causal reading rule
Human narrative clause `X changed because of Y` may be used as a factual claim only when a qualified owner response / material basis directly connects X to Y in CP1/CP0. If only sequence is known, say "Y 之後 X 改變，是否直接因 Y 尚未核對". A free-form LLM interpretation must remain a labelled `RENDERER_INFERENCE`, NEVER silently become CP1 canonical truth.

## Report intelligence vs raw summary
The valuable output is not a transcript or seat-by-seat rollcall. It is a **claim/objection/response/stance-change map rendered in readable causal prose**:
~~~text
Human Mandate → initial paths
               ↘ objection CHALLENGES claim
                 ↘ owner CONSUMES? ↘ owner RESPONDS_TO? 
                   ↘ explicit material basis → owner KEEP / REVISE / HOLD
                     ↘ revised options + surviving contrary claims
                       ↘ current qualified standing + human gate
~~~
Do not infer `CONSUMED` from `DELIVERED` or `AGREED` from `RESPONDED`.

## Architecture boundary
~~~text
CP0 exact human/seat/expert/tool sources
 + CP1 qualified objects/typed edges
 + CP2 current state/standing/lineage
 + actual permitted L8 Light Trace result refs (if relevant)
→ L9 DAIL-declared COUNCIL_NARRATIVE_PROJECTOR (when bound/authorized)
→ Secretariat CP3 human projection (report + optional citations)
→ Human reader / qualified Decision Request if gate exists
~~~
**No backwards arrow from the report to CP1.** Human reaction/new evidence creates a NEW raw input and is admitted through the ordinary governance route, not silently injected from a report.

## Reader-centered explanation contract
Every material claim in the full report should be:
- comprehensible without DAIL keys;
- linkable to event/claim/source or mark interpretation/unknown;
- faithful to historical time and who owns the position;
- specific about whether an objection changed a stance;
- explicit about what remains uncertain;
- clear about what, if anything, the human can decide now.

**Storytelling allowed, fictionalizing governance not allowed.**
