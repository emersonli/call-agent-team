# Team Orchestrator Examples

## 示例 1: MVP 开发 - 电商小程序（应用研发团队）

### 用户输入
```
我想做一个电商小程序，有商品展示、购物车、支付功能，预算 10 万，1 个月上线
```

### AI 分析过程

**Step 1: 任务分析** - 识别为软件开发领域
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
  },
  "domain": "software-development"
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
          "allocation": 1.0
        }
      ]
    },
    {
      "name": "设计与开发",
      "duration": "2.5 weeks",
      "roles": [
        {
          "roleId": "frontend-dev",
          "title": "前端工程师",
          "count": 1,
          "allocation": 1.0
        },
        {
          "roleId": "backend-dev",
          "title": "后端工程师",
          "count": 1,
          "allocation": 1.0
        }
      ]
    }
  ],
  "totalEstimatedCost": 98000,
  "estimatedDuration": "4 weeks"
}
```

---

## 示例 2: 政策制定 - 环保新规（政府行政团队）

### 用户输入
```
需要制定一个新的环保政策，涉及排污标准设定、违规处罚措施、执行监督机制
```

### AI 分析过程

**Step 1: 任务分析** - 识别为政府行政领域
```bash
python scripts/analyze_task.py "环保政策，排污标准，处罚措施，执行监督"
```

输出：
```json
{
  "scenarioId": "policy-making",
  "complexity": "complex",
  "constraints": {},
  "domain": "government-administration"
}
```

**Step 2: 团队匹配** - 选择三省六部制
```bash
python scripts/calculate_team_size.py configs/teams/government-team.yaml complex policy-making
```

**Step 3: 输出团队配置**
```json
{
  "teamType": "government-team",
  "scenario": "policy-making",
  "taskName": "环保政策制定",
  "complexity": "complex",
  "workflow": "三省六部制",
  "phases": [
    {
      "phase": "提案",
      "name": "政策提案",
      "responsible": "生态环境部/地方政府",
      "output": "奏折/提案"
    },
    {
      "phase": "起草",
      "name": "起草诏令",
      "department": "中书省",
      "roles": [
        {
          "roleId": "zhongshu-ling",
          "title": "中书令",
          "count": 1,
          "allocation": 1.0,
          "responsibility": "主持诏令起草"
        },
        {
          "roleId": "zhongshu-shilang",
          "title": "中书侍郎",
          "count": 2,
          "allocation": 1.0,
          "responsibility": "具体撰写"
        }
      ],
      "output": "诏令草稿"
    },
    {
      "phase": "审议",
      "name": "审议封驳",
      "department": "门下省",
      "roles": [
        {
          "roleId": "shizhong",
          "title": "侍中",
          "count": 1,
          "allocation": 1.0,
          "responsibility": "主持审议"
        },
        {
          "roleId": "jishizhong",
          "title": "给事中",
          "count": 2,
          "allocation": 1.0,
          "responsibility": "详细审核"
        }
      ],
      "activities": [
        "审核合法性",
        "评估影响",
        "可提出异议或封还重拟"
      ],
      "output": "审核意见"
    },
    {
      "phase": "批准",
      "name": "皇帝批准",
      "responsible": "最高决策者",
      "output": "正式诏令"
    },
    {
      "phase": "执行",
      "name": "组织实施",
      "department": "尚书省 + 相关部门",
      "roles": [
        {
          "roleId": "minister-head",
          "title": "生态环境部尚书",
          "count": 1,
          "allocation": 1.0,
          "responsibility": "牵头实施"
        },
        {
          "roleId": "xing-ministry-official",
          "title": "刑部官员",
          "count": 1,
          "allocation": 0.5,
          "responsibility": "法律条文制定"
        }
      ],
      "output": "执果"
    },
    {
      "phase": "监督",
      "name": "监督考核",
      "responsible": ["门下省", "吏部"],
      "activities": [
        "检查执行情况",
        "评估政策效果",
        "奖惩相关官员"
      ],
      "output": "考核报告"
    }
  ],
  "estimatedDuration": "6-8 weeks",
  "characteristics": [
    "决策、审议、执行三分离",
    "相互制衡",
    "逐级汇报"
  ]
}
```

---

## 示例 3: 官员任免 - 地方知府选拔（政府行政团队）

### 用户输入
```
江南某府知府职位空缺，需要选拔新任官员，请组织考察和任命
```

### AI 分析

**场景识别**: `personnel-appointment`  
**复杂度**: `medium`  
**主导部门**: 吏部

### 输出团队配置

```json
{
  "teamType": "government-team",
  "scenario": "personnel-appointment",
  "taskName": "知府选拔任命",
  "complexity": "medium",
  "workflow": "简化流程",
  "departments": [
    {
      "name": "吏部",
      "role": "主导",
      "activities": [
        "考察候选人资格",
        "查阅政绩档案",
        "组织面试考核",
        "提出推荐名单"
      ],
      "roles": [
        {
          "roleId": "li-minister",
          "title": "吏部尚书",
          "count": 1,
          "allocation": 1.0
        },
        {
          "roleId": "kaogong-official",
          "title": "考功司官员",
          "count": 2,
          "allocation": 1.0
        }
      ]
    },
    {
      "name": "中书省",
      "role": "参与",
      "activities": ["起草任命诏书"],
      "roles": [
        {
          "roleId": "zhongshu-sheren",
          "title": "中书舍人",
          "count": 1,
          "allocation": 0.5
        }
      ]
    },
    {
      "name": "门下省",
      "role": "监督",
      "activities": ["审核任命程序", "提出异议（如有）"],
      "roles": [
        {
          "roleId": "jianyi-dafu",
          "title": "谏议大夫",
          "count": 1,
          "allocation": 0.5
        }
      ]
    }
  ],
  "estimatedDuration": "2-3 weeks",
  "process": [
    "吏部考察 → 提出推荐",
    "中书省起草诏书 → 门下省审核",
    "皇帝批准 → 正式任命"
  ]
}
```

---

## 示例 4: 大型工程 - 黄河治理（政府行政团队）

### 用户输入
```
黄河泛滥成灾，需要组织大规模治理工程，包括加固堤坝、疏浚河道、移民安置
```

### AI 分析

**场景识别**: `infrastructure-project`  
**复杂度**: `very_complex`  
**主导部门**: 工部

### 输出团队配置

```json
{
  "teamType": "government-team",
  "scenario": "infrastructure-project",
  "taskName": "黄河治理工程",
  "complexity": "very_complex",
  "duration": "6-12 months",
  "leadDepartment": "工部",
  "coordination": [
    {
      "department": "工部",
      "role": "总负责",
      "responsibilities": [
        "工程规划设计",
        "组织施工",
        "质量监督"
      ],
      "roles": [
        {
          "roleId": "gong-minister",
          "title": "工部尚书",
          "count": 1
        },
        {
          "roleId": "engineer-chief",
          "title": "工匠总管",
          "count": 3
        },
        {
          "roleId": "surveyor",
          "title": "测量师",
          "count": 10
        }
      ]
    },
    {
      "department": "户部",
      "role": "资金保障",
      "responsibilities": [
        "财政拨款",
        "粮食供应",
        "移民补偿"
      ],
      "roles": [
        {
          "roleId": "hu-minister",
          "title": "户部尚书",
          "count": 1
        },
        {
          "roleId": "finance-official",
          "title": "财政官员",
          "count": 5
        }
      ]
    },
    {
      "department": "兵部",
      "role": "人力支援",
      "responsibilities": [
        "征调民夫",
        "派遣士兵协助",
        "维持秩序"
      ],
      "roles": [
        {
          "roleId": "bing-official",
          "title": "兵部官员",
          "count": 2
        }
      ]
    },
    {
      "department": "刑部",
      "role": "执法监督",
      "responsibilities": [
        "惩治贪污",
        "处理纠纷"
      ],
      "roles": [
        {
          "roleId": "xing-official",
          "title": "刑部官员",
          "count": 2
        }
      ]
    }
  ],
  "estimatedBudget": "50-100 万两白银",
  "riskFactors": [
    "工期长，需防中途变故",
    "资金量大，需防贪污",
    "民工众多，需防骚乱"
  ]
}
```

---

## 示例 5: 跨领域协作 - 教育改革

### 用户输入
```
要推行新的科举制度改革，减少诗赋比重，增加实务策论，同时建立新式学堂
```

### AI 分析

这是一个**跨部门协作**的复杂任务：
- **礼部**：主导科举改革
- **工部**：学堂建设
- **户部**：经费保障

### 输出团队配置

```json
{
  "teamType": "government-team",
  "scenario": "cross-department-reform",
  "taskName": "科举制度改革",
  "complexity": "very_complex",
  "leadDepartment": "礼部",
  "supportingDepartments": ["工部", "户部"],
  "workflow": {
    "phase1": {
      "name": "方案制定",
      "lead": "礼部 + 中书省",
      "duration": "4 weeks"
    },
    "phase2": {
      "name": "审议批准",
      "lead": "门下省",
      "duration": "2 weeks"
    },
    "phase3": {
      "name": "分头实施",
      "parallel": [
        {"dept": "礼部", "task": "改革考试内容"},
        {"dept": "工部", "task": "建设新式学堂"},
        {"dept": "户部", "task": "拨付经费"}
      ],
      "duration": "12 weeks"
    },
    "phase4": {
      "name": "验收总结",
      "lead": ["门下省", "吏部"],
      "duration": "2 weeks"
    }
  }
}
```

---

## 对比分析

### 不同领域的决策流程对比

| 维度 | 应用研发 | 政府行政 |
|-----|---------|---------|
| 决策模式 | 产品经理主导 | 三省分工制衡 |
| 流程特点 | 敏捷迭代 | 严格层级 |
| 文档要求 | PRD+ 技术文档 | 诏令 + 奏折 |
| 审批环节 | 较少（灵活） | 较多（严谨） |
| 适用场景 | 商业产品 | 公共政策 |

### 渐进式披露实践

**Level 1 (本文档)**: 快速了解各领域如何使用  
**Level 2**: 查看具体配置文件了解详细架构  
**Level 3**: 参考 `reference.md` 深度案例

---

## 使用建议

1. **明确任务领域**：先判断是软件/政府/企业/教育等领域
2. **选择对应配置**：加载相应的团队配置文件
3. **调整规模**：根据复杂度和约束条件微调
4. **参考历史**：查看类似项目的实际执行情况
