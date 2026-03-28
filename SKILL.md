---
name: team-orchestrator
version: 2.0.0
description: 为多 Agent 框架智能匹配专业团队。根据任务领域自动选择团队类型（应用研发/政府行政/企业运营等），评估规模确定人员配置，考虑约束条件优化组合。Use when managing multi-agent workflows, building specialized teams, or organizing agent roles for complex projects.
description_zh: 为多 Agent 框架自动匹配专业团队。支持应用研发、政府行政、企业运营等多种团队类型，从需求分析到执行全流程覆盖。
---

# Team Orchestrator - 智能团队编排器

## 核心理念

本技能采用**渐进式披露**原则设计：
- **通用流程**：所有团队类型共享的核心逻辑（本节内容）
- **领域特定**：各行业的专业团队配置（见 `configs/teams/` 目录）
- **按需加载**：只在识别到相关任务时才加载详细的领域知识

## 核心工作流程

### 1. 任务分析与领域识别

分析用户任务，确定所属领域：

| 领域关键词 | 匹配团队 | 配置文件 |
|-----------|---------|---------|
| 软件、App、网站、开发、测试 | 应用研发团队 | `configs/teams/dev-team.yaml` |
| 政策、政务、决策、行政、法规 | 政府行政团队 | `configs/teams/government-team.yaml` |
| 企业、管理、运营、市场、人力 | 企业运营团队 | `configs/teams/corporate-team.yaml` (待扩展) |
| 教育、课程、培训、教学 | 教育团队 | `configs/teams/education-team.yaml` (待扩展) |

### 2. 团队匹配

根据识别的领域：
1. 加载对应的团队配置文件
2. 匹配场景配方（Scenario-based Recipes）
3. 引用角色定义库

### 3. 规模计算

执行 `scripts/calculate_team_size.py`：
- 基于任务复杂度
- 考虑预算、时间等约束
- 参考历史数据优化

### 4. 输出配置

生成 JSON 格式的团队配置：
```json
{
  "teamType": "<团队类型>",
  "scenario": "<场景>",
  "complexity": "<复杂度>",
  "phases": [...],
  "roles": [...],
  "totalEstimatedCost": <成本>,
  "estimatedDuration": "<周期>"
}
```

## 通用决策矩阵

### 复杂度评估标准

| 等级 | 特征 | 工期范围 | 团队规模 |
|-----|------|---------|---------|
| 简单 | 单一目标，流程清晰 | <2 周 | 2-4 人 |
| 中等 | 多模块协作，标准流程 | 2-8 周 | 5-10 人 |
| 复杂 | 系统性工程，跨部门 | 2-6 月 | 10-20 人 |
| 极复杂 | 长期项目，多层级 | >6 月 | 20+ 人 |

### 约束处理规则

**预算不足** (< 标准成本 70%):
- 提示风险并建议调整方案
- 优先保证核心功能
- 考虑分阶段实施

**时间紧急** (< 标准工期 70%):
- 增加人力投入 (1.3-1.5x)
- 启用快速响应模式
- 简化流程和文档

**质量要求高**:
- 强制配置 QA/监督角色
- 增加评审环节
- 延长测试/验证周期

## 领域特定工作流

### 应用研发领域

适用场景：软件开发、网站建设、移动应用等

**典型阶段**:
1. 需求分析与 PRD (10-15%)
2. UI/UX 设计 (15-20%)
3. 开发实现 (40-50%)
4. 测试与修复 (20-25%)
5. 部署上线 (5-10%)

**快速参考**:
```yaml
场景：MVP 开发
配置：1 产品 +1 前端 +1 后端 +0.5 测试
工期：2-4 周
成本：5-15 万
```

详细配置见：[configs/teams/dev-team.yaml](configs/teams/dev-team.yaml)

### 政府行政领域

适用场景：政策制定、行政管理、公共事务等

**典型流程** (三省六部制):
1. 提案阶段 → 任何部门或地方
2. 起草诏令 → 中书省
3. 审议封驳 → 门下省
4. 皇帝批准 → 最高决策者
5. 分派执行 → 尚书省
6. 具体实施 → 六部
7. 监督考核 → 门下省 + 吏部

**快速参考**:
```yaml
场景：政策制定
配置：中书省 (起草) + 门下省 (审议) + 相关部委 (执行)
工期：4-8 周
特点：决策、审议、执行三分离
```

详细配置见：[configs/teams/government-team.yaml](configs/teams/government-team.yaml)

## 调用示例

### 示例 1: 软件开发任务
```
用户：我想做一个电商小程序，有商品展示、购物车、支付功能，预算 10 万，1 个月上线

AI 处理流程:
1. 识别关键词："小程序"、"开发"、"支付" → dev-team
2. 识别场景："MVP"、"1 个月" → mvp-development
3. 执行：python scripts/calculate_team_size.py configs/teams/dev-team.yaml medium
4. 输出团队配置（详见 examples.md）
```

### 示例 2: 政策制定任务
```
用户：需要制定一个新的环保政策，涉及排污标准、处罚措施、执行监督

AI 处理流程:
1. 识别关键词："政策"、"环保"、"标准" → government-team
2. 识别场景："政策制定" → policy-making
3. 执行：python scripts/calculate_team_size.py configs/teams/government-team.yaml complex
4. 输出配置：中书省起草 + 门下省审议 + 生态环境部执行
```

### 示例 3: 模糊任务
```
用户：我们有个项目需要人手，你看着安排

AI 处理流程:
1. 追问关键信息：
   - "请问是什么类型的项目？（软件/政策/活动/其他）"
   - "预期多久完成？"
   - "大概多少人合适？"
2. 根据回答匹配合适的团队类型
```

## 可扩展架构

### 添加新团队类型

在 `configs/teams/` 下创建新的 YAML 文件：

```yaml
teamType: your-team-type
name: 你的团队名称
description: 描述

organizationalStructure:
  # 组织架构定义

scenarios:
  # 场景配方
  
roleDefinitions:
  # 角色定义
```

### 添加新角色

在 `configs/roles/` 下创建角色定义文件，包含：
- 基本信息
- 能力模型
- 职责边界
- 最佳实践
- 工作量估算

## 脚本工具

| 脚本 | 功能 | 用法 |
|-----|------|-----|
| `analyze_task.py` | 任务分析 | `python scripts/analyze_task.py "任务描述"` |
| `calculate_team_size.py` | 计算团队规模 | `python scripts/calculate_team_size.py <config> <复杂度>` |
| `match_roles.py` | 角色匹配 | `python scripts/match_roles.py <关键词>` |
| `validate_config.py` | 配置验证 | `python scripts/validate_config.py <配置文件>` |

## 渐进式披露策略

本技能的设计遵循渐进式披露原则：

### Level 1: 通用知识（本文档）
- 核心工作流程
- 通用决策矩阵
- 基本调用方法

### Level 2: 领域概览（本文档章节）
- 各领域快速参考
- 典型场景和配置
- 领域特色说明

### Level 3: 详细配置（独立配置文件）
- 完整的团队配置
- 详细的角色定义
- 具体的工作流程

### Level 4: 最佳实践（docs/ 目录下按领域分类）
- [软件研发参考](docs/software-development-reference.md) - 软件开发深度指南
- [政府行政参考](docs/government-administration-reference.md) - 三省六部制详解
- 常见问题解答
- 优化建议

**使用建议**:
- 日常使用：阅读 Level 1-2 即可
- 深度定制：参考 Level 3-4
- AI 调用：根据需要动态加载对应层级的知识

## 相关资源

**核心文档**:
- [使用示例](examples.md) - 实际案例演示
- [软件研发参考](docs/software-development-reference.md) - 软件开发深度指南
- [政府行政参考](docs/government-administration-reference.md) - 三省六部制详解
- [GitHub 仓库](https://github.com/emersonli/call-agent-team) - 源代码

**团队配置**:
- [应用研发团队](configs/teams/dev-team.yaml) - 软件开发
- [政府行政团队](configs/teams/government-team.yaml) - 政策制定
- _更多团队类型持续更新中..._

**协作模式库**:
- [软件研发协作模式](collaboration/software/) - agile-sprint, rapid-response
- _更多领域协作模式规划中..._

---

**版本**: 2.0.0  
**最后更新**: 2026-03-28  
**维护者**: emersonli
