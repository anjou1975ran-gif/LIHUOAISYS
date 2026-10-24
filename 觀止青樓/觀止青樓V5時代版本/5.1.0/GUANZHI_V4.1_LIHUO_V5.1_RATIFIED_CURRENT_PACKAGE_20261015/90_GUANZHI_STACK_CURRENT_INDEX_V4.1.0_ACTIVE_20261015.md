# GUANZHI STACK CURRENT INDEX
## V4.1.0 / V2.3.2 / V3.3.20｜ACTIVE｜2026-10-15

```yaml
GUANZHI_STACK_CURRENT_INDEX:
  id: GUANZHI_STACK_CURRENT_INDEX_20261015

  status:
    - ACTIVE
    - HUMAN_RATIFIED
    - DOCUMENT_LEVEL_CURRENT
    - NOT_HOST_DEPLOYMENT
    - NOT_RUNTIME_RECEIPT

  coordinated_activation_event_id:
    GUANZHI_V4_1_0_COORDINATED_RATIFICATION_ACTIVATION_20261015

  central_lihuo:
    stack: V5.1.0
    current_index_sha256: "bf4ab8e8ac7fb7dcddb313ecaa80e0f253c7213699b9a89b5463bebd83c8a458"
    protocol_sha256: "b0cf16f39f8aa0d971068cdf09b06039e66640c2545a8f7810ee1d216597acee"
    lighter_sha256: "1b64aeb40be2ae514e25ea15da653d8b41edd20472df57f9f2f49b320a1b7a10"
    main_sha256: "2c1a090ac10304b6e78e7daf1372842ab082db2c7bb9d0af9b2ae349c6baa28c"

  guanzhi_four_main_files:
    core:
      version: V4.1.0
      file: 01_GUANZHI_RUNTIME_CORE_V4.1.0_FULL_BODY_RATIFIED_CURRENT_20261015.md
      sha256: "811045d64233bc0c6381bc6ecf14e7c67be92dda60157ca55b69bdb703c1b74f"

    world:
      version: V2.3.2_CURRENT
      file: 02_GUANZHI_WORLD_V2.3.2_CURRENT_FULL_V5.1_POINTER_20261015.md
      sha256: "9bd36c38c3bd32a968debb27ae71e59515f100ffa4a30aca614153f53da38daf"
      semantic_change: NONE

    director:
      version: V4.1.0
      file: 03_GUANZHI_DIRECTOR_V4.1.0_FULL_BODY_RATIFIED_CURRENT_20261015.md
      sha256: "79d93866b11aedcd96ccfd3c14c923df857ebe46d07790b68ba6ec6f636fbdf1"

    character_pool:
      version: V3.3.20_CURRENT
      file: 04_GUANZHI_CHARACTER_POOL_LCAPG_V3.3.20_CURRENT_71_UNCHANGED.md
      sha256: "4bea6ad2383ef76e9d5cdae0389ddbe7962d92c39cf798acc270ba3a03c4df95"
      change: NONE

  locks:
    exactly_four_main_files: true
    no_fifth_main_file: true
    world_pointer_embedded_in_world_main_file: true
    no_staged_current_interval: true

  boundaries:
    host_deployment_proven: false
    runtime_execution_proven: false
```

`CURRENT` here means document-governance Current. It does not prove Host deployment or runtime execution.
