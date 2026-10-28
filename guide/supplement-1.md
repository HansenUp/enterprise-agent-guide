# 补充概念一 模型与可信输出

## Transformer / Attention / MoE（Transformer 架构／注意力机制／Mixture of Experts 混合专家） 【基础】

Transformer 通过注意力等模块组织 token 之间的信息；Attention 的 Q、K、V 用于计算关联与汇聚表示。RoPE 是一种位置编码方法。MoE 通过路由选择部分专家网络参与计算，“专家”是模型内部参数模块，不是多个业务 Agent。架构影响推理资源与部署，应用选型仍须实测。[S40]

## Pre-training / Post-training / In-Context Learning（预训练／后训练／上下文学习） 【基础】

预训练学习广泛统计模式；后训练进一步调整指令遵循、偏好或推理等行为；上下文学习通过当前示例影响本次输出，通常不更新权重。把知识放进 Prompt 不等于训练模型，购买基础模型也不等于获得完整可运行 Agent。

## RLHF / RLAIF / RLVR（基于人类反馈／AI 反馈／可验证奖励的强化学习） 【条件】

RLHF 使用人类反馈，RLAIF 使用 AI 反馈，RLVR 使用可验证奖励。PPO 是一种策略优化算法，GRPO 利用组内相对奖励构造优化信号；具体训练方法并不能单独保证业务能力。企业应用团队通常先完善数据和评测，再决定是否有必要进入训练层。[S42]

## Hallucination / Grounding / Abstention（幻觉／事实依据／拒答） 【基础】

幻觉是生成不受事实支持的内容；Grounding 将输出约束到给定证据或环境；Abstention 在证据不足时拒绝下确定结论。低温、引用、微调和多个模型表决都不能完全消除幻觉。平台应能返回“证据不足”和待确认事项，而不是强迫每次填满所有字段。

## Self-Consistency / Best-of-N（自洽采样／多候选择优） 【条件】

Self Consistency 采样多条推理路径并汇聚答案；Best of N 生成多个候选，再由评分器选取。收益依赖候选多样性和评判可靠性，会增加成本；它们与多 Agent 协作并非同义。同一偏差下的多数票不能替代事实核验。[S41]

## Benchmark / Data Contamination（基准测试／数据污染） 【基础】

公开基准便于比较某类能力，但任务分布、工具环境和评分方式可能不匹配企业应用。训练见过题目、评测泄漏或只挑选成功运行都会造成高估。架构选型应以业务保留集和故障测试为主，公开分数用于筛选候选而非直接验收。

<!-- 来源链接：使 GitHub 上的 [Sxx] 可点击；交互版构建时忽略 -->

[S40]: https://arxiv.org/abs/1706.03762
[S41]: https://arxiv.org/abs/2203.11171
[S42]: https://arxiv.org/abs/2402.03300
