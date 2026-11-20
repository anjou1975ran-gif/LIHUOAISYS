# INITIAL MATERIAL L8｜B 身份同一性與架構轉向
**Cycle:** SEED-L8-B-INITIAL-001 • SAME_MODEL_MULTI_ROLE_REFERENCE
**Preconditions:** `METHOD/EV_A0_B_METHOD_DECISION.md` → `OBSERVATION/EV_A1_B_FIRST_OBSERVATION.md` → THIS initial material L8. Pack receipt as applicable. **No other seat's current stance used as scoped input.**
**Council Round:** R001, not equal to L8 internal R1/R2/R3+.

## R1｜互競的初始 premises
- **B-P1** 極短格言／幾條規則作 SEED。**對抗：** 容易記住，但移除來源/適用目標後變成一般口號
- **B-P2** 最小必要關係圖作 SEED。**對抗：** 可以把責任、否定、材料觸發表示成條件關係，但可能只停在符號圖
- **B-P3** 連同所有 Canonical Events 與舊對話交付。**對抗：** 完整可追，卻可能讓舊答案先行並增加污染
- **B-P4** 針對再生目標保存：身份不變量、可變項、失敗條件與來源解參照。**對抗：** 條件可精確，但是否足以再生仍待驗證
**Point-Light / O9 R1:** 以上候選及反例是可見的文本競爭，不聲稱讀到模型隱藏內部狀態。
**T1 SEED-B-T1：** Minimal 不是短；需要先知道『哪一種東西應保持同一』。舊立場不是身份，責任歸屬/合法改判與來源結構可能才是。

## R2｜本席消費 T1
從『記憶壓縮』轉向 `TARGET_RELATIVE_REGENERATIVE_RELATION_SET`：目標 T、必要不變量 I、生成依賴 G、允許變化 V、不能偷升格的約束 C、剝除測試 F。舊案例只作可解參照來源，不納入預設 P0。尚未規定唯一資料格式。
**O9 R2：** 將反對/黑區帶回本席，不代寫他席立場。
**T2 SEED-B-T2：** 結構身份以『在新題中是否再次形成責任與可追改判可能性』判定，而非逐字或結論相同。

## Post-R2 Premise Audit
- `MULTIPLE_PREMISE_FAMILIES=true`：來源／觀察／資格／反證／成本是否成立不由單一縮短文本假設決定。
- `R3_REQUIRED=true`：仍有未解的最小性/再生/史料/行為對照前提。

## R3｜保留異議並跨前提核查
檢查哲學方法盲點：一張自洽的圖可以沒有任何實際再生。目標若設得太窄會把舊組織/流程永遠固定；若太寬任何回答都過關。需要後續 D 的可觀測反證及 N1 的行為標準來壓制概念自洽。
**O9 R3：** 反例仍存在，沒有因寫了 Main 就自行升格。
**T3 SEED-B-T3：** 交還可追查的概念物件與尚未證實項目。

## Main + Origin Declared Typed Objects
```yaml
origin_actor: CORE_SEAT_B
origin_event_id: SEED-EV-A2-B
main_ref: SEED-B-MAIN-001
main: "TARGET_RELATIVE_SEED_RELATION_MODEL"
origin_semantic_type: "PROBLEM_REFRAME+STRUCTURE_CANDIDATE"
stance: "SEED_IDENTITY_IS_GENERATIVE_CONSTRAINTS_NOT_HISTORICAL_ANSWERS"
surviving_objection: "形式關係圖不等於會真的長出判斷；可能過度制度凍結"
source_method_decision: SEED-EV-A0-B
source_first_observation: SEED-EV-A1-B
external_expert_return: NONE
proposal_originated: NONE
```

## SGER / Compact L8 receipt
```yaml
SGER:
  cycle: SEED-L8-B-INITIAL-001
  R1: [B-P1,B-P2,B-P3,B-P4]
  T1: SEED-B-T1
  R2_consumes_T1: true
  T2: SEED-B-T2
  post_R2_premise_audit: MULTIPLE
  R3_plus: [R3]
  T3: SEED-B-T3
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: SEED-B-MAIN-001
  TM: "SEED-B-TM: no historical validation/seat qualification backfill"
  Vertical_Acceptance: CONDITIONAL_CONCEPT_OBJECT
  execution_identity: SAME_MODEL_MULTI_ROLE_REFERENCE
  evidence_status: TEXTUAL_REFERENCE_NOT_INDEPENDENT_MODEL_PROOF
```
**Compact L8 Cycle Receipt:** R1→T1→R2 consumes T1→T2→plurality check→R3/T3→MAIN/TM/SGER; this is an observable scoped judgement, not actual independent model invocation.
