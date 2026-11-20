# 04｜Git 寫入與回讀證據｜PSO-RADAR-004
**Event kind:** POST_CYCLE_EXTERNAL_PERSISTENCE_VERIFICATION / APPEND-ONLY.
**Date:** 2026-11-21. **Repository:** `anjou1975ran-gif/LIHUOAISYS` / `main`.
**Purpose:** Distinguish L8's inline-structured evidence at assembly from actually persisted repository bytes. This record does NOT make an unmeasured Radar effect true.

## Observed successful Git API writes
1. Commit `caccede9cba2251e92e79f8430449bd8447f680c`: initial 5 files (README, 00, 01, E05, E06). Git ref update returned `success=true`.
2. Commit `91ec3b5e9a5965227415663ce772e0ed3652cfdb`: full 02 L8 SGER and 03 result/audit request. Git ref update returned `success=true`.
3. Direct post-commit `fetch_file` returned complete readable bytes and these exact Git blob SHAs (GitHub wrapper returned content):
   - README.md: `5a75ed989281c8edec311b0b75c6708337f4b4f4`
   - 00_SOURCE_AND_DESIGN.md: `98b4ad8a2d32b5f6b9ed01ae53e73d5682eed208`
   - E05_SYNTHETIC_EVENT.md: `86a1d40254b17ce086b85d3cbf458385a8084ece`
   - E06_SYNTHETIC_EVENT.md: `73669696628b6c26155459f16776bd727d2cbcfe`
   - 01_RADAR_EVENT_SCAN.md: `286ae1f5617b292bd7568b88904b53b24923688a`
   - 02_L8_FULL_SGER_AND_RECEIPT.md: `c865d579c88a12f957360dd4e14f6cdfb29a1591`
   - 03_RESULT_AND_AUDIT_REQUEST.md: `be2f9d765b7734fcc99c86741b72f20f1977e90c`
4. The full 02 was read back at 26,678 JavaScript code units; presence of `LAMP_STATE_R1/R2/R3`, T1/T2/T3, SGER, MAIN RETURN, POST_MAIN GOVERNANCE verified by checks. That is a **text-content and path presence check**, not an independent legal or philosophical qualification ruling.
5. This file and root index are submitted in a following Git Commit; verify that commit head and these two paths by a subsequent fetch.

## Updated standing after successful readback
```yaml
TASK: PSO-RADAR-RESIDENT-DELTA-004
L8_EVIDENCE_ASSEMBLY_STANDING: INLINE_STRUCTURED_RECORD
POST_WRITE_EVIDENCE_PERSISTENCE: EXTERNAL_DURABLE_VERIFIED_FOR_7_FILES
GIT_COMMIT_1: caccede9cba2251e92e79f8430449bd8447f680c
GIT_COMMIT_2: 91ec3b5e9a5965227415663ce772e0ed3652cfdb
DOES_NOT_UPGRADE:
  - RADAR_CAUSAL_EFFECT
  - INDEPENDENT_RADAR_SERVICE
  - MULTI_AGENT_INDEPENDENCE
  - HOST_DEPLOYMENT
  - MAIN_PROVIDER_INDEPENDENCE
  - TRAINING_PASS
  - AUDIT_APPROVAL_BY_DUIDUI
```

**Time/lineage note:** The preceding SGER marked external durability pending because it was prepared BEFORE the Git calls were successful. This NEW record supplies post-write evidence; it does **not** rewrite the earlier receipt to pretend the result had already existed. 
