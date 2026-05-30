# AUTO_Model2.0.spfx 解压清单

- 源文件: `02_Simulation_Model\AUTO_Model2.0.spfx`
- 大小: 9,862,106 bytes
- ZIP 内条目: 354

## 压缩说明

All Models/*.xml and Project.xml use Simio proprietary compression (magic bytes b2o_/prF). Plain XML parsing requires Simio export or IDE.

仍可稳定读取的内容:
- ZIP 目录结构（对象类型、Process 逻辑文件名）
- `Results/Model/TableStates.sqlite`（上次运行残留的状态表）
- `04_Output/*.csv` 导出的 Results 报告
- `modeldetail/` 截图与架构文档

## ZIP 顶层分类

| 分类 | 文件数 |
|------|--------|
| Data | 47 |
| Models | 291 |
| Project.xml | 1 |
| Results | 3 |
| ViewInfos | 12 |

## 模型对象类型（Models/ 下文件夹）

- **AllocatePath**
- **BG_Server** — Processes: BG_changover
- **BasicNode** — Processes: OnEntered, OnEnteredParking, OnEnteredToAssociatedObject, OnExited, OnRunEnding, OnRunInitialized, TransferFailureLogic
- **Combiner** — Processes: FailureOccurrenceLogic, OnBalkedEnteringMemberInputBuffer, OnBalkedEnteringOutputBuffer, OnBalkedEnteringParentInputBuffer, OnCapacityChanged, OnCapacityReleased, OnEnteredMemberInputBuffer, OnEnteredOutputBuffer, OnEnteredParentInputBuffer, OnEnteredProcessing, OnEvaluatingSeizeRequest, OnExitedOutputBuffer, OnExitedProcessing, OnFailed, OnRenegedFromMemberInputBuffer, OnRenegedFromOutputBuffer, OnRenegedFromParentInputBuffer, OnRepaired, OnRunEnding, OnRunInitialized, OnSecondaryResourceCapacityChanged, PerformProcessingTask
- **DA_Server** — Processes: DA_changover
- **DS_Server** — Processes: DS_changover
- **Model** — Processes: BG_Release, DA_Failed_1, DA_Failed_10, DA_Failed_11, DA_Failed_12, DA_Failed_13, DA_Failed_14, DA_Failed_15, DA_Failed_16, DA_Failed_17, DA_Failed_18, DA_Failed_19, DA_Failed_2, DA_Failed_3, DA_Failed_4, DA_Failed_5, DA_Failed_6, DA_Failed_7, DA_Failed_8, DA_Failed_9, DA_Release, DA_Repaired, DS_Release, Input_Separator_Mag_Entered, MemberOutput_Separator_MLot_Entered, MemberOutput_Separator_SubLot_Entered, Mold_Release, OutputWB1, OutputWB10, OutputWB11, OutputWB12, OutputWB13, OutputWB14, OutputWB15, OutputWB16, OutputWB17, OutputWB18, OutputWB19, OutputWB2, OutputWB20, OutputWB21, OutputWB22, OutputWB23, OutputWB24, OutputWB3, OutputWB4, OutputWB5, OutputWB6, OutputWB7, OutputWB8, OutputWB9, ParentOutput_Separator_MLot_Entered, ParentOutput_Separator_SubLot_Entered, Taping_Failed1, Taping_Failed2, Taping_Release, Taping_Repaired, WB_Failed_1, WB_Failed_10, WB_Failed_11, WB_Failed_12, WB_Failed_13, WB_Failed_14, WB_Failed_15, WB_Failed_16, WB_Failed_17, WB_Failed_18, WB_Failed_19, WB_Failed_2, WB_Failed_20, WB_Failed_21, WB_Failed_22, WB_Failed_23, WB_Failed_24, WB_Failed_3, WB_Failed_4, WB_Failed_5, WB_Failed_6, WB_Failed_7, WB_Failed_8, WB_Failed_9, WB_Release, WB_Repaired, Worker_BG_RunInitialized, Worker_DA_RunInitialized, Worker_DS_RunInitialized, Worker_Mold_RunInitialized, Worker_Taping_RunInitialized, Worker_WB_RunInitialized, outputBG1, outputBG2, outputBG3, outputBG4, outputBG5, outputBG6, outputBG7, outputBG8, outputBG9, outputDA1, outputDA10, outputDA11, outputDA12, outputDA13, outputDA14, outputDA15, outputDA16, outputDA17, outputDA18, outputDA19, outputDA2, outputDA3, outputDA4, outputDA5, outputDA6, outputDA7, outputDA8, outputDA9, outputDS1, outputDS2, outputDS3, outputDS4, outputDS5, outputDS6, outputMold1, outputMold2, outputMold3, outputMold4, outputMold5, outputMold6, outputMold7, outputTaping1, outputTaping2
- **Mold_Server** — Processes: Mold_changover
- **MovePath**
- **MyWorker**
- **OrderEntity** — Processes: OnEnteredFreeSpace, Process1
- **Path** — Processes: OnCollided, OnCollisionCleared, OnEntered, OnExited, OnReachedEnd, OnRunEnding, OnRunInitialized, OnTrailingEdgeEntered, OnTurnedAround
- **Separator** — Processes: FailureOccurrenceLogic, OnBalkedEnteringInputBuffer, OnBalkedEnteringMemberOutputBuffer, OnBalkedEnteringParentOutputBuffer, OnCapacityChanged, OnCapacityReleased, OnEnteredInputBuffer, OnEnteredMemberOutputBuffer, OnEnteredParentOutputBuffer, OnEnteredProcessing, OnEvaluatingSeizeRequest, OnExitedMemberOutputBuffer, OnExitedParentOutputBuffer, OnExitedProcessing, OnFailed, OnRenegedFromInputBuffer, OnRenegedFromMemberOutputBuffer, OnRenegedFromParentOutputBuffer, OnRepaired, OnRunEnding, OnRunInitialized, OnSecondaryResourceCapacityChanged, PerformProcessingTask
- **Server** — Processes: FailureOccurrenceLogic, OnBalkedEnteringInputBuffer, OnBalkedEnteringOutputBuffer, OnCapacityChanged, OnCapacityReleased, OnEnteredInputBuffer, OnEnteredOutputBuffer, OnEnteredProcessing, OnEvaluatingSeizeRequest, OnExitedOutputBuffer, OnExitedProcessing, OnFailed, OnRenegedFromInputBuffer, OnRenegedFromOutputBuffer, OnRepaired, OnRunEnding, OnRunInitialized, OnSecondaryResourceCapacityChanged, PerformProcessingTask
- **Sink** — Processes: OnEnteredInputBuffer, OnRunEnding, OnRunInitialized
- **Source** — Processes: OnBalkedEnteringOutputBuffer, OnEnteredOutputBuffer, OnEnteredProcessing, OnEntityArrival, OnExitedOutputBuffer, OnExitedProcessing, OnRenegedFromOutputBuffer, OnRunEnding, OnRunInitialized, OnStopEventOccurred
- **Taping_Server** — Processes: Taping_changover
- **TransferNode** — Processes: OnEntered, OnEnteredFromAssociatedObject, OnEnteredParking, OnEnteredToAssociatedObject, OnExited, OnRunEnding, OnRunInitialized, RoutingOutLogic, TransferFailureLogic
- **WB_Server** — Processes: WB_changover
- **Worker** — Processes: Allocate, Dropoff, OnCapacityAllocated, OnCapacityChanged, OnCapacityReleased, OnCapacityReservationCancelled, OnCreated, OnEnteredFreeSpace, OnEvaluatingRiderAtPickup, OnEvaluatingRiderReservation, OnEvaluatingSeizeRequest, OnMinimumDwellTimeExpired, OnMoveRequestAccepted, OnNewSeizeRequest, OnRiderLoaded, OnRiderLoading, OnRiderReservationAccepted, OnRiderUnloaded, OnRiderUnloading, OnRunEnding, OnRunInitialized, OnVisitingNode, Pickup, PlanVisit

## ViewInfos（主模型实例视图）

- `AllocatePath_ModelViewInfo.xml`
- `BG_Server_ModelViewInfo.xml`
- `DA_Server_ModelViewInfo.xml`
- `DS_Server_ModelViewInfo.xml`
- `Model_Experiment1_ExperimentViewInfo.xml`
- `Model_ModelViewInfo.xml`
- `Mold_Server_ModelViewInfo.xml`
- `MovePath_ModelViewInfo.xml`
- `MyWorker_ModelViewInfo.xml`
- `OrderEntity_ModelViewInfo.xml`
- `Taping_Server_ModelViewInfo.xml`
- `WB_Server_ModelViewInfo.xml`

## 内嵌 SQLite（TableStates）

- **Table_Orders_States_InteractiveValues**: 0 rows, columns: `__RowIndex`
- **Table_Orders_States_PlanValues**: 0 rows, columns: `__RowIndex`
- **Table_Materials_States_InteractiveValues**: 0 rows, columns: `__RowIndex`
- **Table_Materials_States_PlanValues**: 0 rows, columns: `__RowIndex`
- **Table_MachineConfig_States_InteractiveValues**: 0 rows, columns: `__RowIndex`
- **Table_MachineConfig_States_PlanValues**: 0 rows, columns: `__RowIndex`
- **Table_SetupConfig_States_InteractiveValues**: 0 rows, columns: `__RowIndex`
- **Table_SetupConfig_States_PlanValues**: 0 rows, columns: `__RowIndex`
- **Table_Table1_States_InteractiveValues**: 0 rows, columns: `__RowIndex`
- **Table_Table1_States_PlanValues**: 0 rows, columns: `__RowIndex`

## 内嵌 Results 文件

- `Results/Model/Constraint.log`
- `Results/Model/Interactive_Results.stats`
- `Results/Model/TableStates.sqlite`
