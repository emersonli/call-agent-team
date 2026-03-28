# Team Orchestrator Examples

## 示例 1: MVP 开发 - 电商小程序

### 用户输入
```
我想做一个电商小程序，有商品展示、购物车、支付功能，预算 10 万，1 个月上线
```

### AI 分析过程

**Step 1: 任务分析**
```bash
python scripts/analyze_task.py "电商小程序，商品展示、购物车、支付，预算 10 万，1 个月"
```

输出：
```json
{
  "scenarioId": "mvp-development",
  "complexity": "medium",
  "constraints": {
    "budget": 100000,
    "deadline": "1 个月",
    "urgent": true
  }
}
```

**Step 2: 团队规模计算**
```bash
python scripts/calculate_team_size.py configs/teams/dev-team.yaml medium mvp-development
```

**Step 3: 输出团队配置**
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
        {
          "roleId": "product-manager",
          "title": "产品经理",
          "count": 1,
          "allocation": 1.0,
          "keyDeliverables": ["PRD 文档", "产品原型", "用户故事"]
        }
      ]
    },
    {
      "name": "设计与开发",
      "duration": "2.5 weeks",
      "roles": [
        {
          "roleId": "product-manager",
          "title": "产品经理",
          "count": 1,
          "allocation": 0.3
        },
        {
          "roleId": "ui-ux-designer",
          "title": "UI/UX 设计师",
          "count": 1,
          "allocation": 0.5,
          "keyDeliverables": ["UI 设计稿", "交互规范"]
        },
        {
          "roleId": "frontend-dev",
          "title": "前端工程师",
          "count": 1,
          "allocation": 1.0,
          "focus": "小程序开发"
        },
        {
          "roleId": "backend-dev",
          "title": "后端工程师",
          "count": 1,
          "allocation": 1.0,
          "focus": "API 和数据库"
        }
      ]
    },
    {
      "name": "测试与上线",
      "duration": "3-5 days",
      "roles": [
        {
          "roleId": "qa-engineer",
          "title": "测试工程师",
          "count": 1,
          "allocation": 1.0
        },
        {
          "roleId": "backend-dev",
          "title": "后端工程师",
          "count": 1,
          "allocation": 0.5,
          "focus": "部署"
        }
      ]
    }
  ],
  "collaborationMode": "rapid-response",
  "totalEstimatedCost": 98000,
  "estimatedDuration": "4 weeks",
  "budgetStatus": "within_budget"
}
```

---

## 示例 2: 完整应用 - 企业 CRM 系统

### 用户输入
```
需要开发一个企业级 CRM 系统，包含客户管理、销售漏斗、报表分析、权限管理，工期 3 个月，质量要求高
```

### AI 分析

**场景识别**: `full-stack-app`  
**复杂度**: `complex`  
**约束**: 工期 12 周，质量要求高

### 输出团队配置

```json
{
  "teamType": "dev-team",
  "scenario": "full-stack-app",
  "taskName": "企业 CRM 系统开发",
  "complexity": "complex",
  "phases": [
    {
      "name": "需求分析与规划",
      "duration": "2 weeks",
      "roles": [
        {
          "roleId": "product-manager",
          "title": "产品经理",
          "count": 1,
          "allocation": 1.0,
          "deliverables": ["MRD", "PRD", "用户故事地图", "原型图"]
        }
      ]
    },
    {
      "name": "UI/UX 设计",
      "duration": "3 weeks",
      "roles": [
        {
          "roleId": "product-manager",
          "count": 1,
          "allocation": 0.3
        },
        {
          "roleId": "ui-ux-designer",
          "title": "UI/UX 设计师",
          "count": 1,
          "allocation": 1.0,
          "deliverables": ["视觉规范", "完整设计稿", "交互原型", "切图资源"]
        }
      ]
    },
    {
      "name": "迭代开发",
      "duration": "8 weeks",
      "iterations": 4,
      "sprintLength": "2 weeks",
      "roles": [
        {
          "roleId": "product-manager",
          "count": 1,
          "allocation": 0.5
        },
        {
          "roleId": "frontend-dev",
          "title": "前端工程师",
          "count": 2,
          "allocation": 1.0,
          "specialization": [
            {"level": "senior", "count": 1, "focus": "架构 + 核心模块"},
            {"level": "mid", "count": 1, "focus": "页面开发"}
          ]
        },
        {
          "roleId": "backend-dev",
          "title": "后端工程师",
          "count": 2,
          "allocation": 1.0,
          "specialization": [
            {"level": "architect", "count": 1, "focus": "系统设计"},
            {"level": "developer", "count": 1, "focus": "业务逻辑"}
          ]
        },
        {
          "roleId": "qa-engineer",
          "title": "测试工程师",
          "count": 1,
          "allocation": 0.5,
          "entryPoint": "Sprint 1 中期"
        }
      ]
    },
    {
      "name": "系统测试与修复",
      "duration": "2 weeks",
      "roles": [
        {
          "roleId": "qa-engineer",
          "count": 1,
          "allocation": 1.0,
          "focus": ["系统集成测试", "性能测试", "安全测试"]
        },
        {
          "roleId": "frontend-dev",
          "count": 2,
          "allocation": 0.5,
          "focus": "Bug 修复"
        },
        {
          "roleId": "backend-dev",
          "count": 2,
          "allocation": 0.5,
          "focus": "Bug 修复"
        }
      ]
    },
    {
      "name": "部署上线",
      "duration": "1 week",
      "roles": [
        {
          "roleId": "devops-engineer",
          "title": "运维工程师",
          "count": 1,
          "allocation": 1.0,
          "deliverables": ["CI/CD", "生产环境", "监控告警"]
        },
        {
          "roleId": "backend-dev",
          "count": 1,
          "allocation": 0.5
        }
      ]
    }
  ],
  "collaborationMode": "agile-sprint",
  "mandatoryRoles": ["qa-engineer"],
  "codeReviewRequired": true,
  "testCoverageMin": 0.7,
  "totalEstimatedCost": 485000,
  "estimatedDuration": "12 weeks"
}
```

---

## 示例 3: 紧急项目 - 活动落地页

### 用户输入
```
下周有个营销活动，急需做一个 H5 落地页，有抽奖、分享、排行榜功能，很着急！
```

### AI 分析

**场景识别**: `mvp-development`  
**复杂度**: `simple` (但时间紧急)  
**约束**: 工期 1 周，urgent=true

### 输出团队配置

```json
{
  "teamType": "dev-team",
  "scenario": "mvp-development",
  "taskName": "营销活动 H5 落地页",
  "complexity": "simple",
  "urgency": "high",
  "phases": [
    {
      "name": "需求确认",
      "duration": "0.5 day",
      "roles": [
        {
          "roleId": "product-manager",
          "count": 1,
          "allocation": 0.5
        }
      ]
    },
    {
      "name": "快速开发",
      "duration": "3-4 days",
      "roles": [
        {
          "roleId": "ui-ux-designer",
          "count": 1,
          "allocation": 0.5
        },
        {
          "roleId": "frontend-dev",
          "count": 2,
          "allocation": 1.0,
          "note": "因时间紧急，增加 1 名前端并行开发"
        },
        {
          "roleId": "backend-dev",
          "count": 1,
          "allocation": 1.0
        }
      ]
    },
    {
      "name": "测试上线",
      "duration": "1-2 days",
      "roles": [
        {
          "roleId": "qa-engineer",
          "count": 1,
          "allocation": 1.0
        },
        {
          "roleId": "devops-engineer",
          "count": 1,
          "allocation": 0.5
        }
      ]
    }
  ],
  "collaborationMode": "rapid-response",
  "rushMultiplier": 1.5,
  "totalEstimatedCost": 45000,
  "estimatedDuration": "1 week",
  "riskWarning": "工期紧张，建议砍掉非核心功能"
}
```

---

## 示例 4: 角色能力查询

### 查询前端工程师的详细定义

```bash
cat configs/roles/frontend-dev.yaml
```

关键信息：
- **能力模型**: HTML/CSS(专家), JavaScript/TS(专家), React/Vue(高级)
- **典型职责**: 页面实现、API 对接、单元测试、Code Review
- **协作边界**: 
  - 与产品：需求评审、功能验收
  - 与设计：UI 走查、还原度确认
  - 与后端：接口定义、联调测试
- **工作量估算**: 
  - 简单页面：4-8 小时
  - 中等功能：16-40 小时
  - 复杂交互：40-120 小时

---

## 示例 5: 协作模式选择

### 场景 A: 常规产品开发
推荐：`agile-sprint`
- 2 周一个 Sprint
- 完整的 Scrum 仪式
- 适合稳定迭代

### 场景 B: 紧急 MVP
推荐：`rapid-response`
- 日循环开发
- 最小化流程
- 每晚可演示

### 决策依据
| 维度 | Agile Sprint | Rapid Response |
|-----|-------------|----------------|
| 工期 | 2 周+ | <2 周 |
| 流程开销 | 中 | 低 |
| 文档要求 | 完整 | 最小化 |
| 适用场景 | 常规项目 | 紧急/MVP |
