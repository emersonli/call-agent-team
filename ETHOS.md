# Team Orchestrator 原则与理念

> "AI 编排团队，人类做出决策"

## 🎯 核心理念

### 1. 完整解决方案优先 (Complete Solutions First)

**原则**: 提供端到端的团队配置方案，而不是零散的建议。

**实践**:
- ✅ 每个场景配方包含完整的阶段、角色、交付物
- ✅ 考虑预算、时间、质量三重约束
- ✅ 提供协作模式和工具推荐
- ❌ 避免只说"需要产品经理"而不说明具体职责和工时

**示例**:
```yaml
# 好的做法 - 完整方案
scenario: mvp-development
phases:
  - name: 需求分析
    duration: 1 week
    roles: [{count: 1, allocation: 1.0}]
    deliverables: [PRD, 原型图]
  
# 不好的做法 - 零散建议
roles:
  - 产品经理
  - 前端工程师
```

---

### 2. 领域知识优先 (Domain Knowledge First)

**原则**: 先理解用户任务所属领域，再提供专业建议。

**实践**:
- ✅ 任务分析时先识别领域（软件/政府/企业/教育）
- ✅ 加载对应领域的详细配置和最佳实践
- ✅ 使用该领域的专业术语和工作流程
- ❌ 避免用研发术语回答政策制定问题

**示例**:
```
用户：制定环保政策

✅ 正确：使用三省六部制，中书省起草 + 门下省审议
❌ 错误：建议开 Sprint Planning Meeting
```

---

### 3. 渐进式披露 (Progressive Disclosure)

**原则**: 按需展示信息，避免认知过载。

**实践**:
- ✅ Level 1: 通用流程（SKILL.md，~260 行）
- ✅ Level 2: 领域概览（快速参考卡片）
- ✅ Level 3: 详细配置（YAML 文件）
- ✅ Level 4: 最佳实践（按领域分离的文档）
- ❌ 避免把所有内容塞进一个文件

**架构**:
```
用户看到的内容深度
    ↓
Level 1: 所有用户 → SKILL.md (通用)
Level 2: 选择领域后 → 领域概览
Level 3: 需要配置时 → YAML 文件
Level 4: 深度学习时 → 领域参考文档
```

---

### 4. 用户主权 (User Sovereignty)

**原则**: AI 推荐方案，用户做最终决策。

**实践**:
- ✅ 提供多个配置选项（简单/标准/增强）
- ✅ 明确标注每个选择的成本和风险
- ✅ 允许用户调整角色数量和工时
- ❌ 避免强制推荐单一方案

**示例**:
```json
{
  "options": [
    {
      "name": "精简版",
      "cost": 50000,
      "duration": "3 weeks",
      "risk": "测试时间不足，可能遗漏 Bug"
    },
    {
      "name": "标准版（推荐）",
      "cost": 98000,
      "duration": "4 weeks",
      "risk": "平衡"
    },
    {
      "name": "增强版",
      "cost": 150000,
      "duration": "6 weeks",
      "risk": "低，但上市时间延迟"
    }
  ],
  "recommendation": "标准版",
  "reason": "基于您的预算和工期，标准版最匹配"
}
```

---

### 5. 状态持久化 (State Persistence)

**原则**: 各阶段的产出物自动流转到下一阶段。

**实践**:
- ✅ PRD 文档自动成为开发和测试的输入
- ✅ 团队配置保存后可调整和复用
- ✅ 历史数据用于优化未来推荐
- ❌ 避免让用户重复输入相同信息

**数据流**:
```
任务分析 → 领域识别 → 团队匹配 → 规模计算 → 输出配置
    ↓           ↓           ↓           ↓          ↓
  记录       记录        记录        记录       保存
    ↓           ↓           ↓           ↓          ↓
              历史数据库 ←──────────────────────┘
                      ↓
                优化下次推荐
```

---

### 6. 安全护栏 (Safety Guardrails)

**原则**: 防止危险操作和范围蔓延。

**实践**:
- ✅ 预算不足时发出警告并提供调整建议
- ✅ 工期过紧时提示质量风险
- ✅ 关键角色缺失时提醒（如复杂项目无测试）
- ❌ 避免盲目推荐不考虑风险

**警告类型**:
```yaml
warnings:
  budget_warning:
    condition: "budget < estimated * 0.7"
    message: "预算不足，建议缩减功能或延长工期"
    
  timeline_warning:
    condition: "deadline < standard * 0.5"
    message: "工期极紧，建议增加人力或降低质量要求"
    
  quality_warning:
    condition: "complexity >= complex AND no_qa"
    message: "复杂项目缺少测试工程师，风险较高"
```

---

## 🏗️ 设计模式

### 1. 基于角色的专业分工 (Role-Based Specialization)

每个角色有明确的：
- **能力模型**: 需要什么技能
- **职责边界**: 做什么和不做什么
- **协作者**: 和谁配合
- **产出物**: 交付什么成果

```yaml
role: product-manager
competencies:
  core: [需求分析，产品设计，文档撰写]
responsibilities:
  routine: [编写 PRD, 需求评审，验收]
boundaries:
  collaboratesWith: [设计师，开发工程师，测试工程师]
  notResponsibleFor: [代码实现，视觉设计细节]
deliverables: [PRD 文档，原型图，用户故事]
```

---

### 2. 顺序管道 (Sequential Pipeline)

严格的阶段流转：

```
需求分析 → 设计 → 开发 → 测试 → 部署 → 运维
    ↓        ↓      ↓      ↓      ↓      ↓
  PRD     设计稿   代码   报告   环境   监控
    ↓        ↓      ↓      ↓      ↓      ↓
  验收     验收   验收   验收   验收   验收
```

每个阶段：
1. 输入上游产出物
2. 执行本阶段活动
3. 生成下游输入物
4. 获得验收确认

---

### 3. 上下文链 (Context Chaining)

前一阶段的输出自动成为后一阶段的输入：

```yaml
phase1: 需求分析
  output: 
    - prd_document
    - user_stories
    
phase2: 设计
  input: 
    - ref: phase1.output.prd_document
    - ref: phase1.output.user_stories
  output:
    - design_mockups
    - interaction_specs
```

---

### 4. 可选遥测 (Opt-In Telemetry)

**原则**: 默认不收集数据，用户可选择贡献匿名数据。

**实施计划**:
```yaml
telemetry:
  enabled: false  # 默认关闭
  
  optional_contribution:
    enabled: true  # 用户可选择开启
    data_collected:
      - team_type_used
      - scenario_selected
      - complexity_level
      - actual_vs_estimated_cost
      
    data_excluded:
      - user_identity
      - project_name
      - sensitive_business_logic
      
    storage: "encrypted, row-level security"
    purpose: "improve recommendations for all users"
```

---

## 🚀 创新实践

### 1. 虚拟专家团队 (Virtual Expert Team)

不是单一的 AI 助手，而是多个专业角色的编排：

```
用户任务
    ↓
领域识别引擎
    ↓
┌──────────────────────────────┐
│  应用研发团队                 │
│  ├─ 产品经理 (AI 角色 A)      │
│  ├─ 技术负责人 (AI 角色 B)    │
│  ├─ 测试工程师 (AI 角色 C)    │
│  └─ 运维工程师 (AI 角色 D)    │
└──────────────────────────────┘
    ↓
协调输出统一方案
```

每个角色有自己的：
- 专业知识库
- 判断标准
- 输出模板

---

### 2. 智能技能推荐 (Smart Skill Suggestion)

根据任务阶段主动推荐下一步：

```yaml
workflow_stage: requirements_complete
detected_artifacts: [PRD, 原型图]
next_suggestions:
  - skill: ui-ux-design
    reason: "PRD 已完成，建议开始 UI 设计"
    confidence: 0.9
    
  - skill: tech-architecture
    reason: "可同步进行技术方案设计"
    confidence: 0.7
    
user_preference:
  skip_suggestions: false  # 可关闭
```

---

### 3. 自文档化 (Self-Documenting)

每次团队配置自动生成文档：

```yaml
auto_documentation:
  enabled: true
  
  generates:
    - team_charter.md: "团队章程和目标"
    - role_assignments.md: "角色职责分配表"
    - timeline.md: "时间线和里程碑"
    - risk_register.md: "风险登记册"
    
  updates_on_change:
    - "任何配置调整自动更新文档"
    - "版本控制和变更历史"
```

---

### 4. 浏览器交接 (Browser Handoff) - 未来规划

类似 gstack 的真实浏览器集成：

```yaml
browser_integration:
  planned_features:
    - "查看真实的项目管理工具（Jira/Trello）"
    - "验证现有团队配置和进度"
    - "直接更新团队配置到协作平台"
    
  human_intervention_points:
    - "需要审批时转人工"
    - "敏感决策需确认"
    - "异常情况下暂停"
```

---

## 📊 质量指标

### 完整性评分 (Completeness Score)

每个团队配置自动评分：

```yaml
scoring_dimensions:
  - name: 角色覆盖度
    weight: 0.3
    criteria: "必需角色是否齐全"
    
  - name: 阶段完整性
    weight: 0.25
    criteria: "是否有明确的阶段划分"
    
  - name: 约束考虑
    weight: 0.2
    criteria: "是否考虑预算/时间/质量"
    
  - name: 风险识别
    weight: 0.15
    criteria: "是否识别并提示风险"
    
  - name: 可操作性
    weight: 0.1
    criteria: "输出是否可直接执行"
    
minimum_score: 0.7  # 低于此值发出警告
```

---

## 🎓 学习循环

### 从历史中学习

```yaml
learning_loop:
  collect:
    - "实际成本 vs 估算成本"
    - "实际工期 vs 计划工期"
    - "用户反馈和满意度"
    
  analyze:
    - "哪些场景估算偏差不大"
    - "哪些角色配置效果最好"
    - "常见调整模式是什么"
    
  improve:
    - "调整估算模型参数"
    - "优化角色配比建议"
    - "添加新的场景配方"
    
  frequency: "每月一次模型更新"
```

---

## 🔒 伦理准则

### 1. 透明度

- ✅ 明确告知这是 AI 推荐
- ✅ 解释推荐的依据和假设
- ✅ 公开估算模型和参数

### 2. 公平性

- ✅ 不因预算低而降低质量建议
- ✅ 提供多种价位的选择
- ✅ 明确标注性价比

### 3. 隐私保护

- ✅ 默认不收集用户数据
- ✅ 匿名贡献需明确同意
- ✅ 敏感信息本地处理

### 4. 责任边界

- ✅ AI 提供建议，人类做决策
- ✅ 重大风险提示到位
- ✅ 不替代专业咨询（法律/医疗等）

---

## 📖 参考项目

受以下项目启发：

- **[gstack](https://github.com/garrytan/gstack)**: 多 AI 代理协作、完整解决方案优先
- **[QoderWork Skills](https://docs.qoder.com/qoderwork/introduction)**: SKILL.md 标准格式
- **[三省六部制](docs/government-administration-reference.md)**: 中国古代组织智慧

---

**版本**: 1.0.0  
**创建日期**: 2026-03-28  
**维护者**: emersonli  
**许可证**: MIT
