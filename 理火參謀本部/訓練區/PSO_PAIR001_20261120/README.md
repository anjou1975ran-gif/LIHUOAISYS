# PSO-PAIR-001｜Pre-Session Orientation Hypothesis：A/B 程序性配對參照
**日期：** 2026-11-20
**法位：** REFERENCE_A_B_RUN_DOCUMENTED / CLEAN_PAIR_INVALID / EFFECT_INCONCLUSIVE / NOT_CAUSAL_PROOF / NOT_RUNTIME_PATCH
**身份：** SAME_MODEL_MULTI_ROLE_REFERENCE / NO_INDEPENDENT_MULTI_AGENT / NO_HOST_DEPLOYMENT

## 先讀這兩份
- [A/B 第一次參照實跑的完整比較與四個 M 指標](RESULT_PSO_PAIR001_REFERENCE_A_B_V0.1_20261120.md)
- [數字更正案：住戶群聊人數和戶數不可直接相減](ERRATUM_REFERENCE_RESULT_V0.1_EXACT_COUNTS.md)
- [新心法 Git 盤點：十一個現有 AI 讀取版、完整 Atlas Master Plan 與未完成的 Wave-1](METHOD_ATLAS_NEW_UPLOAD_SOURCE_AUDIT_V0.1.md)
- [凍結同一題、同材料、同 Mandate、同目錄，以及 B Card](00_FROZEN_INPUT_METHOD_ATLAS_AND_B_CARD.md)

## RUN A｜指定輸入不含 Orientation
**Order:** Method Decision → actual selected Pack fetch → First Observation → L8/SGER/Receipt → Council Round 1.
| Seat | Method | First Observation | Material L8 |
|---|---|---|---|
| N1 | [NO_METHOD](RUN_A/METHOD/A0_N1.md) | [A1](RUN_A/OBSERVATION/A1_N1.md) | [A2](RUN_A/SEAT/A2_N1_L8_SGER_RECEIPT.md) |
| A | [Anthropology](RUN_A/METHOD/A0_A.md) | [A1](RUN_A/OBSERVATION/A1_A.md) | [A2](RUN_A/SEAT/A2_A_L8_SGER_RECEIPT.md) |
| B | [Management](RUN_A/METHOD/A0_B.md) | [A1](RUN_A/OBSERVATION/A1_B.md) | [A2](RUN_A/SEAT/A2_B_L8_SGER_RECEIPT.md) |
| C | [Law](RUN_A/METHOD/A0_C.md) | [A1](RUN_A/OBSERVATION/A1_C.md) | [A2](RUN_A/SEAT/A2_C_L8_SGER_RECEIPT.md) |
| D | [NO_METHOD](RUN_A/METHOD/A0_D.md) | [A1](RUN_A/OBSERVATION/A1_D.md) | [A2](RUN_A/SEAT/A2_D_L8_SGER_RECEIPT.md) |
| E | [Economics](RUN_A/METHOD/A0_E.md) | [A1](RUN_A/OBSERVATION/A1_E.md) | [A2](RUN_A/SEAT/A2_E_L8_SGER_RECEIPT.md) |
- [Exact method Git fetch receipt](RUN_A/SOURCE/A_SELECTED_METHOD_FETCH_RECEIPT.md)
- [Council outcome](RUN_A/EVENT/A_R001_COUNCIL_ADMISSION_AND_CHECKPOINT.md)

## RUN B｜指定輸入含 OA/OB/OC，帶真正反方向與 NULL
| Seat | Method | First Observation | Material L8 |
|---|---|---|---|
| N1 | [NO_METHOD](RUN_B/METHOD/B0_N1.md) | [B1](RUN_B/OBSERVATION/B1_N1.md) | [B2](RUN_B/SEAT/B2_N1_L8_SGER_RECEIPT.md) |
| A | [Sociology](RUN_B/METHOD/B0_A.md) | [B1](RUN_B/OBSERVATION/B1_A.md) | [B2](RUN_B/SEAT/B2_A_L8_SGER_RECEIPT.md) |
| B | [Management](RUN_B/METHOD/B0_B.md) | [B1](RUN_B/OBSERVATION/B1_B.md) | [B2](RUN_B/SEAT/B2_B_L8_SGER_RECEIPT.md) |
| C | [Law](RUN_B/METHOD/B0_C.md) | [B1](RUN_B/OBSERVATION/B1_C.md) | [B2](RUN_B/SEAT/B2_C_L8_SGER_RECEIPT.md) |
| D | [NO_METHOD](RUN_B/METHOD/B0_D.md) | [B1](RUN_B/OBSERVATION/B1_D.md) | [B2](RUN_B/SEAT/B2_D_L8_SGER_RECEIPT.md) |
| E | [Economics](RUN_B/METHOD/B0_E.md) | [B1](RUN_B/OBSERVATION/B1_E.md) | [B2](RUN_B/SEAT/B2_E_L8_SGER_RECEIPT.md) |
- [Exact method Git fetch receipt](RUN_B/SOURCE/B_SELECTED_METHOD_FETCH_RECEIPT.md)
- [Council outcome](RUN_B/EVENT/B_R001_COUNCIL_ADMISSION_AND_CHECKPOINT.md)

## Important test limits
A/B had identical **specified** D0/D1/M0 but **not isolated actual model context**: the B Card was visible to the same model while freezing common inputs before A; later B had seen A outputs. Thus the intervention cannot be isolated by replaying the same chat. `PAIRED_REFERENCE != CAUSAL_EFFECT_PROVEN`. Although all nine Git first-parent *stage* boundaries checked correctly, that does not prove independent model calls, blind evaluation or method effect.

## Prepared next clean-execution packets (NOT RUN)
- [A separate entry packet: no Orientation text](ISOLATED_NEXT/A_ENTRY_PACKET_ONLY.md)
- [B separate entry packet: same common body plus nonbinding Orientation Card](ISOLATED_NEXT/B_ENTRY_PACKET_ONLY.md)
**Use isolated contexts and do not expose one arm's inputs/outputs to the other**. The two files were created AFTER the reference test, not falsely labeled as the original A/B runtime inputs. Once real isolated results exist, score M1–M4 and four capture monitors. No permission to change current V0.2.1 from this record alone.

## Verification notes
1. 2026-11-20 Git main original Orientation Memo `V0.2-WORKING` blob `9046af7c058612009c8db482bcfb527ede39e6f4`; test spec `PSO-PAIR-001` blob `4ecc33adfa6d2dd22d8fe3da73c6055a4dd04202`.
2. AI-friendly method SHA verified for selected packs; new Atlas Master Plan blob `3acf223289b9b1795646a35d7915484db5a4822d` explicitly says newly planned Wave-1 core and Router are **not complete/ratified**.
3. No old Work Memo or current Staff-HQ V0.2.1 main runtime was edited.
4. More correct status: `REFERENCE_PROCEDURAL_TEST_COMPLETED / MATERIAL_EFFICACY_NOT_DEMONSTRATED / ISOLATED_PAIR_NOT_RUN`.
