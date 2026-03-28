---
name: team-orchestrator
version: 1.0.0
description: 为多 Agent 框架自动匹配应用研发团队成员。根据任务类型匹配专业角色（产品经理、前端、后端、测试等），评估任务规模确定人员数量，考虑预算和时间约束。Use when managing multi-agent software development workflows, building dev teams, or organizing agent roles for app development projects.
description_zh: 为多 Agent 框架自动匹配应用研发团队成员。从需求细化到 PRD、研发、测试全流程覆盖。
---

# Team Orchestrator - 应用研发团队编排器

## 核心工作流程

### 1. 任务分析
分析用户任务的：
- **任务类型**：识别属于软件开发的哪个阶段（需求分析/设计/开发/测试）
- **复杂度等级**：简单/中等/复杂/极复杂
- **约束条件**：预算上限、时间限制、质量要求

### 2. 团队匹配
读取 `configs/teams/dev-team.yaml` 配置：
- 根据任务场景选择标准配方（MVP/完整应用/遗留重构）
- 引用 `configs/roles/` 下的角色定义
- 应用 `collaboration/` 下的协作模式

### 3. 规模计算
执行 `scripts/calculate_team_size.py`：
- 基于复杂度计算各角色数量
- 考虑预算约束调整配置
- 参考历史数据优化预测

### 4. 输出配置
生成 JSON 格式的团队配置，包含：
- 团队类型和场景
- 各角色的名称、职责、数量、工时
- 推荐的协作模式
- 预计成本和周期

## 快速决策矩阵

| 任务场景 | 简单配置 | 标准配置 | 增强配置 |
|---------|---------|---------|---------|
| MVP 开发 (2-4 周) | 1 产品 +1 全栈 | 1 产品 +1 前端 +1 后端 +0.5 测试 | +1 设计 +1 运维 |
| 完整应用 (2-3 月) | 1 产品 +2 前端 +2 后端 +1 测试 | +1 设计 +0.5 运维 | +1 产品 +1 测试 |
| 大型系统 (3-6 月) | 2 产品 +3 前端 +3 后端 +2 测试 +1 运维 | +2 设计 +1 架构师 | +1 项目经理 |

## 软件开发阶段与角色配比

### 阶段 1: 需求分析与 PRD (占比 10-15%)
**主导角色**: 产品经理  
**参与角色**: 技术负责人、设计师  
**产出物**: PRD 文档、原型图、技术方案

### 阶段 2: 设计与原型 (占比 15-20%)
**主导角色**: UI/UX 设计师  
**参与角色**: 产品经理、前端负责人  
**产出物**: 视觉设计稿、交互原型、设计规范

### 阶段 3: 开发实现 (占比 40-50%)
**主导角色**: 前端工程师、后端工程师  
**参与角色**: 测试工程师（中期介入）  
**产出物**: 可运行的软件系统、API 文档、单元测试

### 阶段 4: 测试与修复 (占比 20-25%)
**主导角色**: 测试工程师  
**参与角色**: 全体开发人员  
**产出物**: 测试报告、Bug 修复、性能优化

### 阶段 5: 部署与上线 (占比 5-10%)
**主导角色**: 运维工程师  
**参与角色**: 后端负责人、测试工程师  
**产出物**: 生产环境、监控体系、用户文档

## 约束处理规则

**预算不足** (< 标准成本 70%):
- 提示用户风险
- 建议缩减范围或延长工期
- 优先保证核心功能

**时间紧急** (< 标准工期 70%):
- 增加人力投入 (1.5x)
- 启用并行工作模式
- 加急费率 (1.5x 成本)

**质量要求高**:
- 强制配置专职测试工程师
- 增加代码审查环节
- 延长测试周期

## 输出示例

```json
{
  "teamType": "dev-team",
  "scenario": "mvp-development",
  "taskName": "电商小程序开发",
  "complexity": "medium",
  "phases": [
    {
      "name": "需求分析与 PRD",
      "duration": "1 week",
      "roles": [
        {"name": "产品经理", "count": 1, "allocation": 1.0}
      ]
    },
    {
      "name": "开发实现",
      "duration": "3 weeks",
      "roles": [
        {"name": "前端工程师", "count": 1, "allocation": 1.0},
        {"name": "后端工程师", "count": 1, "allocation": 1.0},
        {"name": "测试工程师", "count": 1, "allocation": 0.5}
      ]
    }
  ],
  "totalEstimatedCost": 85000,
  "estimatedDuration": "4 weeks",
  "collaborationMode": "agile-sprint"
}
```

## 调用示例

### 示例 1: MVP 开发任务
```
用户：我想做一个电商小程序，有商品展示、购物车、支付功能，预算 10 万，1 个月上线

AI 操作:
1. 识别场景：mvp-development
2. 复杂度：medium
3. 约束：预算 10 万，工期 4 周
4. 执行：python scripts/calculate_team_size.py configs/teams/dev-team.yaml medium
5. 输出团队配置
```

### 示例 2: 完整应用开发
```
用户：需要开发一个企业级 CRM 系统，包含客户管理、销售漏斗、报表分析，工期 3 个月

AI 操作:
1. 识别场景：full-stack-app
2. 复杂度：complex
3. 约束：工期 12 周
4. 执行：python scripts/calculate_team_size.py configs/teams/dev-team.yaml complex
5. 输出团队配置（含专职测试、运维）
```

## 相关资源

- 完整团队配置：[configs/teams/dev-team.yaml](configs/teams/dev-team.yaml)
- 角色详细定义：[configs/roles/](configs/roles/)
- 协作模式：[collaboration/agile-sprint.yaml](collaboration/agile-sprint.yaml)
- 使用示例：[examples.md](examples.md)
- 详细参考：[reference.md](reference.md)

## 脚本工具

| 脚本 | 功能 | 用法 |
|-----|------|-----|
| `analyze_task.py` | 任务分析 | `python scripts/analyze_task.py "任务描述"` |
| `calculate_team_size.py` | 计算团队规模 | `python scripts/calculate_team_size.py <config> <complexity>` |
| `match_roles.py` | 角色匹配 | `python scripts/match_roles.py <task_keywords>` |
| `validate_config.py` | 配置验证 | `python scripts/validate_config.py configs/teams/dev-team.yaml` |
