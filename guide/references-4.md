# 参考资料四与持续更新方法

[S40] Vaswani et al Attention Is All You Need 2017

https://arxiv.org/abs/1706.03762

[S41] Wang et al Self Consistency 2022

https://arxiv.org/abs/2203.11171

[S42] Shao et al DeepSeekMath and GRPO 2024

https://arxiv.org/abs/2402.03300

[S43] AG-UI Introduction

https://docs.ag-ui.com/introduction

[S44] A2UI Documentation

https://a2ui.org/

## 如何维护这份知识体系

每季度检查协议版本、弃用公告、SDK 支持范围和关键依赖；模型变更时运行企业评测集。为每次技术判断保留日期、来源和适用任务，不把动态的 latest 链接当永久版本标识。

建立三份独立清单：概念与设计原则、当前技术组件及版本、企业任务上的实验结果。第一份相对稳定，第二份跟随官方生命周期，第三份决定是否投入生产。发现新术语时，先判断它新增了能力、改进了成本，还是重新命名了既有模式。

## 阅读论文时检查什么

任务及数据是否接近企业场景；对照基线是否足够强；是否包含失败、时延和成本；优势能否在独立任务重现；是否需要企业不具备的训练数据或算力。摘要中的效果不宜直接转化为平台承诺。

## 维护职责

平台团队维护接口、运行、安全和版本；业务团队维护成功定义、知识口径及失败案例；数据团队维护质量、血缘和删除传播；研发团队共同维护评测与运行手册。技术趋势由实验验证，平台能力由可重复交付检验。
