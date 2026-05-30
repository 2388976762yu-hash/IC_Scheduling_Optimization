# AUTO_Model2.0 解压解析摘要

- 源文件: `AUTO_Model2.0.spfx`
- 文件大小: 9,862,106 bytes
- 压缩包条目: 354
- 解析时间: 2026-05-24T11:34:21

## 1. 压缩包结构

| 顶层目录 | 文件数 |
|---------|--------|
| `Models` | 291 |
| `Data` | 47 |
| `ViewInfos` | 12 |
| `Results` | 3 |
| `Project.xml` | 1 |

## 2. XML 可读性说明

- Simio 编码 XML: **308** 个
- 明文 XML: **0** 个
- Process 逻辑文件: **266** 个

> Simio .spfx 内部 Models/*.xml 与 Project.xml 为 Simio 专有编码，不能当作普通 XML 直接解析；结构理解需结合 Architecture 文档、截图与运行报告。

## 3. 模型定义类型（来自压缩包目录结构）

| 类型 | 定义文件数 | 说明 |
|------|-----------|------|
| `Source` | 1 | 订单释放 |
| `Separator` | 1 | 批次拆分（通用模板） |
| `Server` | 1 |  |
| `DS_Server` | 1 | D/S 切割工序 |
| `DA_Server` | 1 | DA 粘片工序 |
| `WB_Server` | 1 | WB 焊线工序 |
| `Mold_Server` | 1 | Mold 塑封工序 |
| `BG_Server` | 1 | B/G 键合研磨工序 |
| `Taping_Server` | 1 | Taping 贴带工序 |
| `Combiner` | 1 | SubLot 合并 |
| `Sink` | 1 | 完成汇点 |
| `Worker` | 1 | 搬运 Worker 模板 |
| `MyWorker` | 1 | 自定义 Worker |
| `Path` | 1 | 路径 |
| `MovePath` | 1 | 搬运路径 |
| `AllocatePath` | 1 | 分配路径 |
| `BasicNode` | 1 | 节点 |
| `TransferNode` | 1 | 转移节点 |
| `OrderEntity` | 1 | 订单实体定义 |
| `Model` | 1 | 顶层 Model 容器 |

## 4. 关键 Process 逻辑文件（部分）

- `Models/BG_Server/Processes/BG_changover.xml`
- `Models/BasicNode/Processes/OnEntered.xml`
- `Models/BasicNode/Processes/OnEnteredParking.xml`
- `Models/BasicNode/Processes/OnEnteredToAssociatedObject.xml`
- `Models/BasicNode/Processes/OnExited.xml`
- `Models/BasicNode/Processes/TransferFailureLogic.xml`
- `Models/Combiner/Processes/OnEnteredMemberInputBuffer.xml`
- `Models/Combiner/Processes/OnEnteredOutputBuffer.xml`
- `Models/Combiner/Processes/OnEnteredParentInputBuffer.xml`
- `Models/Combiner/Processes/OnEnteredProcessing.xml`
- `Models/Combiner/Processes/OnExitedOutputBuffer.xml`
- `Models/Combiner/Processes/OnExitedProcessing.xml`
- `Models/Combiner/Processes/OnFailed.xml`
- `Models/Combiner/Processes/PerformProcessingTask.xml`
- `Models/DA_Server/Processes/DA_changover.xml`
- `Models/DS_Server/Processes/DS_changover.xml`
- `Models/Model/Processes/DA_Failed_1.xml`
- `Models/Model/Processes/DA_Failed_10.xml`
- `Models/Model/Processes/DA_Failed_11.xml`
- `Models/Model/Processes/DA_Failed_12.xml`
- `Models/Model/Processes/DA_Failed_13.xml`
- `Models/Model/Processes/DA_Failed_14.xml`
- `Models/Model/Processes/DA_Failed_15.xml`
- `Models/Model/Processes/DA_Failed_16.xml`
- `Models/Model/Processes/DA_Failed_17.xml`
- `Models/Model/Processes/DA_Failed_18.xml`
- `Models/Model/Processes/DA_Failed_19.xml`
- `Models/Model/Processes/DA_Failed_2.xml`
- `Models/Model/Processes/DA_Failed_3.xml`
- `Models/Model/Processes/DA_Failed_4.xml`
- `Models/Model/Processes/DA_Failed_5.xml`
- `Models/Model/Processes/DA_Failed_6.xml`
- `Models/Model/Processes/DA_Failed_7.xml`
- `Models/Model/Processes/DA_Failed_8.xml`
- `Models/Model/Processes/DA_Failed_9.xml`
- `Models/Model/Processes/Taping_Failed1.xml`
- `Models/Model/Processes/Taping_Failed2.xml`
- `Models/Model/Processes/WB_Failed_1.xml`
- `Models/Model/Processes/WB_Failed_10.xml`
- `Models/Model/Processes/WB_Failed_11.xml`
- ... 另有 59 个

## 5. Experiment 相关文件

- `ViewInfos/Model_Experiment1_ExperimentViewInfo.xml`

## 6. 最新运行报告摘要

### `V2-ResultsViewSampleReport.csv`
- Project: AUTO_Model2.0
- Run Date: 2026/5/23 11:11:56
- Created: {'M_LOT': '283', 'MAG': '1255', 'Order': '41', 'SUB_LOT': '652'}
- Destroyed: {'M_LOT': '283', 'MAG': '1255', 'Order': '41', 'SUB_LOT': '652'}
- Source throughput: 41 | Sink throughput: 628

### `V1_ResultsViewSampleReport.csv`
- Project: AUTO_Model2.0
- Run Date: 2026/5/22 17:48:33
- Created: {'M_LOT': '283', 'MAG': '1255', 'Order': '41', 'SUB_LOT': '652'}
- Destroyed: {'M_LOT': '283', 'MAG': '1255', 'Order': '41', 'SUB_LOT': '652'}
- Source throughput: 41 | Sink throughput: 628


## 7. V1/V2 利用率摘要（来自 v1v2_analysis.json）

### V1(1x)
- DS: avg 13.72%, max 18.19%, count 31
- DA: avg 13.54%, max 25.00%, count 112
- WB: avg 13.42%, max 24.79%, count 284
- MOLD: avg 8.91%, max 9.54%, count 7
- BG: avg 9.04%, max 9.97%, count 17
- Taping: avg 9.11%, max 9.53%, count 8
- Order completion: 41.0/41.0 (100.0%)

### V1-1(3x)
- DS: avg 41.15%, max 43.19%, count 31
- DA: avg 40.76%, max 54.46%, count 112
- WB: avg 40.16%, max 54.64%, count 284
- MOLD: avg 26.73%, max 28.09%, count 7
- BG: avg 27.12%, max 28.15%, count 17
- Taping: avg 27.33%, max 27.83%, count 8
- Order completion: 41.0/41.0 (100.0%)

### V1-2(6x)
- DS: avg 81.85%, max 84.14%, count 31
- DA: avg 67.10%, max 73.50%, count 112
- WB: avg 59.16%, max 67.13%, count 284
- MOLD: avg 32.33%, max 33.51%, count 7
- BG: avg 54.23%, max 55.21%, count 17
- Taping: avg 54.66%, max 54.98%, count 8
- Order completion: 41.0/41.0 (100.0%)

### V1-3(5x)
- DS: avg 68.58%, max 72.52%, count 31
- DA: avg 65.02%, max 74.60%, count 112
- WB: avg 57.62%, max 66.28%, count 284
- MOLD: avg 32.24%, max 34.84%, count 7
- BG: avg 45.19%, max 45.96%, count 17
- Taping: avg 45.55%, max 45.99%, count 8
- Order completion: 41.0/41.0 (100.0%)

### V2(avg)
- DS: avg 13.72%, max 17.06%, count 31
- DA: avg 13.61%, max 22.68%, count 112
- WB: avg 13.42%, max 22.05%, count 284
- MOLD: avg 8.91%, max 9.39%, count 7
- BG: avg 9.04%, max 9.50%, count 17
- Taping: avg 9.11%, max 9.72%, count 8
- Order completion: 41.0/41.0 (100.0%)

### V2-1(5x)
- DS: avg 68.58%, max 72.70%, count 31
- DA: avg 67.70%, max 84.76%, count 112
- WB: avg 65.90%, max 75.82%, count 284
- MOLD: avg 41.52%, max 43.19%, count 7
- BG: avg 45.19%, max 45.72%, count 17
- Taping: avg 45.55%, max 46.07%, count 8
- Order completion: 41.0/41.0 (100.0%)
