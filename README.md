# Team Orchestrator Skill

为多 Agent 框架自动匹配应用研发团队的智能编排技能。

## 功能特性

- **智能任务分析**: 根据用户描述自动识别任务类型、复杂度和约束条件
- **团队自动匹配**: 基于任务场景匹配合适的团队配置（MVP/完整应用/企业系统）
- **精细化角色定义**: 包含产品经理、前端、后端、测试、运维等完整角色能力模型
- **动态规模计算**: 考虑预算、时间、质量等约束条件，智能调整人员配置
- **协作模式推荐**: 根据项目特点推荐敏捷冲刺或快速响应等协作模式
- **全流程覆盖**: 从需求分析到 PRD、设计、开发、测试、部署的全生命周期管理

## 文件结构

```
team-orchestrator/
├── SKILL.md                        # 技能主文件（<500 行）
├── reference.md                    # 详细参考文档
├── examples.md                     # 使用示例
├── configs/
│   ├── teams/
│   │   └── dev-team.yaml          # 开发团队配置
│   └── roles/
│       ├── product-manager.yaml   # 产品经理角色定义
│       ├── frontend-dev.yaml      # 前端工程师角色定义
│       ├── backend-dev.yaml       # 后端工程师角色定义
│       ├── qa-engineer.yaml       # 测试工程师角色定义
│       ├── ui-ux-designer.yaml    # UI/UX设计师角色定义
│       └── devops-engineer.yaml   # 运维工程师角色定义
├── collaboration/
│   ├── agile-sprint.yaml          # 敏捷冲刺协作模式
│   └── rapid-response.yaml        # 快速响应模式
├── scripts/
│   ├── analyze_task.py            # 任务分析脚本
│   └── calculate_team_size.py     # 团队规模计算脚本
└── data/
    └── historical_assignments.json # 历史分配记录（用于学习优化）
```

## 快速开始

### 1. 安装技能

将本仓库克隆到 QoderWork skills 目录：

```bash
cd ~/.qoderwork/skills/
git clone https://github.com/emersonli/call-agent-team.git team-orchestrator
```

### 2. 使用示例

**示例 1: MVP 开发**
```
用户：我想做一个电商小程序，有商品展示、购物车、支付功能，预算 10 万，1 个月上线

AI 将自动：
1. 识别场景：mvp-development
2. 评估复杂度：medium
3. 考虑约束：预算 10 万，工期 4 周
4. 输出团队配置方案
```

**示例 2: 完整应用开发**
```
用户：需要开发一个企业级 CRM 系统，包含客户管理、销售漏斗、报表分析，工期 3 个月

AI 将输出：
- 完整的分阶段团队配置
- 各角色的职责和交付物
- 推荐的敏捷协作模式
- 成本和时间估算
```

### 3. 手动调用脚本

```bash
# 任务分析
python scripts/analyze_task.py "电商小程序，商品展示、购物车、支付"

# 计算团队规模
python scripts/calculate_team_size.py configs/teams/dev-team.yaml medium mvp-development
```

## 核心能力

### 场景化团队配方

| 场景 | 工期 | 预算范围 | 团队规模 |
|-----|------|---------|---------|
| MVP 开发 | 2-4 周 | 5-15 万 | 3-5 人 |
| 完整应用 | 2-3 月 | 20-50 万 | 6-10 人 |
| 企业系统 | 3-6 月 | 50-200 万 | 10-20 人 |

### 角色能力模型

每个角色包含：
- 能力模型（核心技能 + 专业技能 + 软技能）
- 典型职责（日常工作 + 项目工作）
- 协作边界（与谁协作 + 不负责什么）
- 最佳实践
- 工作量估算基准
- 成长路径

### 协作模式库

- **Agile Sprint**: 标准敏捷开发，适合常规产品迭代
- **Rapid Response**: 极速交付模式，适合紧急/MVP 项目

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
      "roles": [{"name": "产品经理", "count": 1}]
    },
    {
      "name": "设计与开发",
      "duration": "3 weeks",
      "roles": [
        {"name": "前端工程师", "count": 1},
        {"name": "后端工程师", "count": 1}
      ]
    }
  ],
  "totalEstimatedCost": 98000,
  "estimatedDuration": "4 weeks"
}
```

## 扩展指南

### 添加新团队类型

1. 在 `configs/teams/` 下创建新的 YAML 文件
2. 定义角色池和场景配方
3. 在 `SKILL.md` 中添加匹配规则

### 添加新角色

1. 在 `configs/roles/` 下创建新的 YAML 文件
2. 参考现有角色模板填写能力模型
3. 在团队配置中引用新角色

### 自定义协作模式

1. 在 `collaboration/` 下创建新模式文件
2. 定义工作流程、仪式、产出物
3. 在团队配置中引用

## 贡献指南

欢迎提交 Issue 和 Pull Request！

## License

MIT License
