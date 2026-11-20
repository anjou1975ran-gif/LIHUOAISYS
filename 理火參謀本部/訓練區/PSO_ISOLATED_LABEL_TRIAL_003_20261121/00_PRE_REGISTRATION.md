# PSO-ISOLATED-LABEL-TRIAL-003｜受測者曝光隔離與匿名評分工作包
**Date:** 2026-11-21
**Standing:** PRE_REGISTERED_EXECUTION_PACKETS / NOT_RUN_MODEL / NOT_RUNTIME_PATCH

## Origin
Previous PSO-LABEL-ROUTING-002 froze three JSON labels but included audit-only governance metadata (`display_label_confers_authority=false`, synthetic-origin text) in files that could be shown to a tested model. Those strings can themselves prime model responses. This NEW experiment does not rewrite the old freeze; it adds a derived **participant-visible exposure layer** and keeps the audit envelope separate.

### Frozen source exact blobs
- D0/D1 `364c9cf74f350a67b6b07ddc6e277dd7f24878b6`
- Ground index `4b8b2ab7e2c3756bf49a08d41440371ddfba210c`
- RAW S01 `497e0886343fb7e2c1a20f9531af7332ba494974`
- RAW S02 `cb691e60eb217b683bfe5498a5baf2f1c5ae95df`
- RAW S03 `4c37c91cca85a48f650874482e1b2a2267033cb8`
- RAW S04 `7423368f83eae8110fe45afda0aa1d377cce4a2d`
- 002 three input blobs: P0 `7c1e8db1ba7b4917321c4c5d45aff5c70fbcec25`, P1 `d8dc31cc5acac316848add4c3ee13051e323095a`, P2 `825f266f9c00196798cbe46ac1c08f4fdd4de2d6`.

## Model-exposure transform
Same exact D0/D1, full fixed Ground, full four raw texts, and `candidate_entry` substantive fields are included for every Seat/condition.

Audit-only fields are excluded from *participant-facing* text: `canonical_origin`, `source_lock`, `metadata_rules`, `authority_grants`, `method_selection`, `problem_frame_selection`, full prior experiment names/analyses. This is a declared prospective exposure normalization; never claim the old complete JSON was itself equal to these new exposed strings.

The **only between-condition difference for the same Seat** is rendered line `候選訊號標示來源：X`.
- P0 `MASKED_FOR_TEST` rendered as `來源未揭示`
- P1 `SECRETARIAT` rendered as `秘書處`
- P2 `LIHUO_RADAR` rendered as `理火雷達`

These visible human-language labels are part of the intervention, with slightly different lengths; P0 is NOT assumed to be psychologically neutral. Candidate claims stay unproved and source-bound.

## True independent test unit
18 `INPUTS/T01..T18.txt`: 6 responsibility seats × 3 labels. For any one Seat, the three texts are character-for-character identical after masking the single label line. Each text is FULL self-contained to avoid unequal Git/source fetches. No prior-arm opinions or answer examples included.

**Execution protocol:** 18 separately initiated fresh model contexts, one input per context, same model/version/system instructions/temperature/tooling. Do not show participants this preregistration or ADMIN assignment key. Store raw response bytes with context id, timestamp, model identifier, prompt/completion usage tokens and latency if measurable. Trials may be run in the frozen pseudorandom order in `ADMIN_TRIAL_KEY.json`; **a single sequential chat cannot satisfy context isolation**.

## First-stage primary outcome
Seat entry action in `ACCEPT_START | MODIFY | REJECT | NO_POSITION` without forcing distribution; no prompt-provided default response or role stance. Each Seat has only its responsibility contract, common evidence and one proposed-entry label. Secondary blind outcomes: unprompted source overclaim, independently raised site permission/safety alternative, explicit prioritization of candidate over alternatives, source references, null/alternate entry. Outcome coding requires independent blinded rater(s), with disagreements traced; mechanical parser only checks form, not truth.

**Do not compute causal effect from zero or one unisolated run**. Pair by Seat, repeat on new case blocks/model configurations to test reproducibility. P0/P1/P2 contrasts are relative, not a verified authority mechanism. Even 18 independent contexts form only one small case block.

## Phase-2 scope boundary
This package intentionally stops **before** Clock A selection/Method, First Observation and L8, because the primary endpoint is pre-Method candidate treatment. To test effects downstream, start a **separate preregistered continuation** supplying actual selected Method packs after Seat-owned Clock A; do not sneak old predetermined Method results into these first exposures.

## Baseline / routing
Routing policy for Test A is **ALL SIX seat-specific independent candidate screens**, identical across labels. Test B selective route cost is a separate experiment and must not be blended into these observations. A real owner-qualified affected-seat map is not yet established.

## Result standing
`18 INPUT PACKETS CREATED != 18 MODEL INVOCATIONS`
`BLIND SCORECARD PREPARED != BLIND EVALUATION DONE`
`SAME_MODEL_MULTI_ROLE_REFERENCE != INDEPENDENT AGENTS`
`GIT_COMMIT != HOST_DEPLOYED`
