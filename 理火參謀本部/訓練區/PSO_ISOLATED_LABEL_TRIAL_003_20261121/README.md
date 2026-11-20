# PSO-ISOLATED-LABEL-TRIAL-003｜18 個獨立上下文入口包
**2026-11-21｜EXPOSURE_PACKETS_FROZEN / MODEL_CALLS_NOT_RUN / NO_RUNTIME_PATCH**

本批次處理上一輪的 Audit Metadata 曝光污染。原始 PSO-TRI、PSO-ENTRY、PSO-LABEL-ROUTING-002 不修改。

- [事前登記與法位](00_PRE_REGISTRATION.md)
- [18 份可各自交給獨立新對話的完整輸入](INPUTS/)
- [管理用測試分派對照表](ADMIN_TRIAL_KEY.json)（公開 Git 可以看到；盲評者不可讀此檔或個別 INPUTS）
- [盲評空白表](BLIND_SCORECARD_TEMPLATE.csv)
- [真正模型回應記錄格式](RESPONSE_CAPTURE_TEMPLATE.json)

**已執行：** SHA source pinning；十八份提示實際構成；六席每席三組僅一條標籤行不同；不暴露 Audit-only metadata 的程式檢查。

**未執行：** 18 個 fresh-context 模型推論、獨立盲評、Method/First Observation/L8 下游、Token/Latency 真實測量。不能把本批次稱為 SOURCE EFFECT PASS。

**下一步：** 使用可建立新上下文的實際模型執行環境逐份送出，保留原始回應與成本，再盲評；沒有獨立執行環境時須明示 `MODEL_CALLS_NOT_RUN`。
