# Team Orchestrator 架构文档

## 系统概览

Team Orchestrator 是一个智能团队编排引擎，根据用户任务自动匹配专业团队配置。

```
┌─────────────────────────────────────────────────────────┐
│                    用户输入                              │
│  "我想做一个电商小程序，预算 10 万，1 个月上线"            │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│              1. 任务分析引擎                             │
│  - 关键词提取                                           │
│  - 领域识别（软件/政府/企业/教育）                       │
│  - 复杂度评估                                           │
│  - 约束条件提取                                         │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│              2. 领域路由                                 │
│  ├─ 应用研发 → configs/teams/dev-team.yaml             │
│  ├─ 政府行政 → configs/teams/government-team.yaml      │
│  └─ 其他领域 → 相应配置文件                            │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│              3. 场景匹配                                 │
│  - 选择场景配方（MVP/完整应用/大型系统）                 │
│  - 加载角色定义库                                       │
│  - 应用协作模式                                        │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│              4. 规模计算引擎                             │
│  - 基于复杂度调整人数                                   │
│  - 考虑预算/时间约束                                    │
│  - 参考历史数据优化                                     │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│              5. 输出生成器                               │
│  - JSON 格式团队配置                                     │
│  - 多方案对比（精简/标准/增强）                         │
│  - 风险提示和建议                                       │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│                    用户输出                              │
│  { teamType, scenario, roles[], cost, duration }        │
└─────────────────────────────────────────────────────────┘
```

---

## 核心组件

### 1. 任务分析器 (Task Analyzer)

**文件**: `scripts/analyze_task.py`

**职责**:
- 解析用户输入的自然语言
- 提取关键词和领域信号
- 评估任务复杂度
- 识别约束条件（预算、时间、质量）

**输入**:
```python
task_description = "电商小程序，商品展示、购物车、支付，预算 10 万，1 个月"
```

**输出**:
```json
{
  "domain": "software-development",
  "scenarioId": "mvp-development",
  "complexity": "medium",
  "constraints": {
    "budget": 100000,
    "deadline": "4 weeks",
    "urgent": true
  },
  "keywords": ["电商", "小程序", "支付"]
}
```

**算法**:
```python
def analyze_task(text):
    # 1. 领域识别
    domain = match_domain_keywords(text)
    
    # 2. 场景匹配
    scenario = match_scenario_keywords(text, domain)
    
    # 3. 复杂度评估
    complexity = calculate_complexity(
        text_length=len(text),
        feature_count=count_features(text),
        integration_points=count_integrations(text)
    )
    
    # 4. 约束提取
    constraints = extract_constraints(text)
    
    return {domain, scenario, complexity, constraints}
```

---

### 2. 领域路由器 (Domain Router)

**文件**: `SKILL.md` + 配置加载逻辑

**职责**:
- 根据领域标识选择配置文件
- 加载对应的团队配置
- 加载角色定义库
- 加载协作模式

**注册表**:
```yaml
domain_registry:
  software-development:
    config: configs/teams/dev-team.yaml
    roles_dir: configs/roles/
    collaboration_dir: collaboration/software/
    reference: docs/software-development-reference.md
    
  government-administration:
    config: configs/teams/government-team.yaml
    roles_dir: configs/roles/government/  # 未来扩展
    collaboration_dir: collaboration/government/
    reference: docs/government-administration-reference.md
```

---

### 3. 场景匹配器 (Scenario Matcher)

**文件**: YAML 配置中的 `scenarios` 字段

**职责**:
- 根据任务特征选择最佳场景配方
- 加载预定义的角色组合
- 应用阶段划分
- 设置默认参数

**匹配逻辑**:
```yaml
# dev-team.yaml 示例
scenarios:
  - scenarioId: mvp-development
    match_keywords: [MVP, 快速验证，最小可行，试水]
    default_complexity: simple
    duration_range: [2, 4]  # weeks
    
  - scenarioId: full-stack-app
    match_keywords: [完整应用，商业级，正式发布]
    default_complexity: complex
    duration_range: [8, 12]
```

---

### 4. 规模计算器 (Team Size Calculator)

**文件**: `scripts/calculate_team_size.py`

**职责**:
- 基于复杂度计算各角色数量
- 考虑预算和时间约束
- 应用调整系数
- 生成成本估算

**计算公式**:
```python
def calculate_role_count(role, complexity, constraints):
    base_count = role['defaultCount']
    
    # 复杂度系数
    complexity_multiplier = {
        'simple': 0.5,
        'medium': 1.0,
        'complex': 1.5,
        'very_complex': 2.0
    }[complexity]
    
    # 预算调整
    if constraints['budget'] < estimated_cost * 0.7:
        budget_factor = 0.7
    elif constraints['budget'] > estimated_cost * 1.5:
        budget_factor = 1.2
    else:
        budget_factor = 1.0
    
    # 时间紧急度
    if constraints.get('urgent'):
        urgency_factor = 1.5
    else:
        urgency_factor = 1.0
    
    # 最终计算
    final_count = min(
        role['maxCount'],
        max(1, int(base_count * complexity_multiplier * budget_factor * urgency_factor))
    )
    
    return final_count
```

---

### 5. 输出生成器 (Output Generator)

**职责**:
- 组装完整的团队配置
- 生成多方案对比
- 添加风险提示
- 格式化输出

**输出结构**:
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
      "completionCriteria": "PRD 评审通过",
      "roles": [...]
    },
    {
      "name": "设计与开发",
      "duration": "2.5 weeks",
      "roles": [...]
    }
  ],
  
  "options": [
    {
      "name": "精简版",
      "cost": 70000,
      "duration": "3 weeks",
      "risks": ["测试不足"]
    },
    {
      "name": "标准版（推荐）",
      "cost": 98000,
      "duration": "4 weeks",
      "risks": []
    }
  ],
  
  "warnings": [],
  "recommendations": ["建议增加 1 名测试"],
  "collaborationMode": "agile-sprint"
}
```

---

## 数据流

### 正向流程

```
用户输入
  ↓
[任务分析器]
  ├─ domain: "software-development"
  ├─ scenario: "mvp-development"
  ├─ complexity: "medium"
  └─ constraints: {...}
  ↓
[领域路由器]
  └─ 加载 configs/teams/dev-team.yaml
  ↓
[场景匹配器]
  └─ 选择 mvp-development 配方
  ↓
[规模计算器]
  ├─ 计算各角色数量
  ├─ 估算成本
  └─ 估算工期
  ↓
[输出生成器]
  └─ JSON 配置 + 多方案 + 风险提示
  ↓
用户输出
```

### 反馈循环

```
用户输出
  ↓
用户选择方案 + 实际执行
  ↓
收集实际数据
  ├─ 实际成本
  ├─ 实际工期
  └─ 用户满意度
  ↓
更新历史数据库
  ↓
优化估算模型参数
  ↓
改进下次推荐
```

---

## 渐进式披露实现

### Level 1: 通用层

**文件**: `SKILL.md` (~260 行)

**内容**:
- 核心工作流程
- 通用决策矩阵
- 基本调用方法
- 领域快速参考

**特点**:
- 所有领域共享
- 保持简洁
- 无领域特定术语

---

### Level 2: 领域层

**文件**: `configs/teams/*.yaml`

**内容**:
- 组织架构定义
- 场景配方库
- 角色池定义
- 协作模式引用

**特点**:
- 按领域分离
- 结构化配置
- 可独立修改

---

### Level 3: 角色层

**文件**: `configs/roles/*.yaml`

**内容**:
- 能力模型详细定义
- 职责边界
- 协作者关系
- 工作量估算基准

**特点**:
- 跨领域复用
- 精细化描述
- 最佳实践

---

### Level 4: 实践层

**文件**: `docs/*-reference.md`

**内容**:
- 完整工作流程详解
- 深度案例分析
- 常见问题解答
- 优化建议

**特点**:
- 按领域分离
- 叙事性文档
- 深度学习材料

---

## 扩展点

### 添加新领域

1. **创建团队配置**:
   ```bash
   configs/teams/new-domain-team.yaml
   ```

2. **创建参考文档**:
   ```bash
   docs/new-domain-reference.md
   ```

3. **更新 SKILL.md**:
   ```markdown
   | 领域关键词 | 匹配团队 | 配置文件 |
   |-----------|---------|---------|
   | 新领域关键词 | new-domain-team | configs/teams/new-domain-team.yaml |
   ```

4. **添加示例**:
   ```bash
   examples.md 中添加新领域示例
   ```

---

### 添加新角色

1. **创建角色定义**:
   ```bash
   configs/roles/new-role.yaml
   ```

2. **在团队配置中引用**:
   ```yaml
   rolePool:
     - roleId: new-role
       roleRef: ../roles/new-role.yaml
       minCount: 0
       maxCount: 5
   ```

3. **在场景中使用**:
   ```yaml
   scenarios:
     - scenarioId: some-scenario
       roles:
         - roleId: new-role
           count: 1
   ```

---

### 添加协作模式

1. **创建模式定义**:
   ```bash
   collaboration/domain/new-mode.yaml
   ```

2. **在团队配置中引用**:
   ```yaml
   collaborationModes:
     - modeRef: ../collaboration/domain/new-mode.yaml
       phase: execution
       weight: 0.8
   ```

---

## 安全护栏

### 预算保护

```yaml
validation_rules:
  budget_minimum:
    rule: "total_cost >= min_project_budget"
    action: warn
    message: "项目预算低于最低要求"
    
  budget_maximum:
    rule: "total_cost <= user_budget * 1.3"
    action: error
    message: "超出预算 30%，请调整范围"
```

### 质量保护

```yaml
quality_gates:
  complex_project_qa:
    condition: "complexity >= complex"
    required_roles: [qa-engineer]
    action: require_or_warn
    
  critical_system_devops:
    condition: "system_type == critical"
    required_roles: [devops-engineer]
    action: require
```

### 时间保护

```yaml
timeline_validation:
  minimum_lead_time:
    rule: "deadline >= minimum_duration"
    action: warn_if_violated
    
  rush_project_warning:
    condition: "deadline < standard_duration * 0.7"
    warnings:
      - "工期紧张，建议增加人力"
      - "可能需要加班"
      - "质量风险增加"
```

---

## 性能优化

### 缓存策略

```yaml
caching:
  team_configs:
    enabled: true
    ttl: 24h
    key: "domain + scenario + complexity"
    
  role_definitions:
    enabled: true
    ttl: 7d
    key: "roleId"
    
  historical_data:
    enabled: true
    refresh: weekly
```

### 懒加载

```yaml
lazy_loading:
  level_1: "always_load"  # SKILL.md
  level_2: "load_on_domain_match"  # 团队配置
  level_3: "load_on_role_need"  # 角色定义
  level_4: "load_on_deep_dive"  # 参考文档
```

---

## 监控指标

### 使用统计

```yaml
metrics:
  usage:
    - total_requests_per_day
    - requests_by_domain
    - most_used_scenarios
    - average_complexity
    
  accuracy:
    - estimated_vs_actual_cost_error
    - estimated_vs_actual_duration_error
    - user_satisfaction_score
    
  performance:
    - average_response_time
    - cache_hit_rate
    - configuration_generation_time
```

---

## 故障恢复

### 降级策略

```yaml
fallback_strategy:
  primary_failure: "使用默认配置"
  secondary_failure: "返回错误并提供手动选项"
  
  graceful_degradation:
    - "配置加载失败 → 使用基础模板"
    - "历史数据不可用 → 使用标准估算"
    - "角色定义缺失 → 使用通用描述"
```

---

## 版本兼容性

```yaml
versioning:
  current: "2.1.0"
  
  breaking_changes:
    - "v2.0.0: 添加多领域支持"
    - "v2.1.0: 重构渐进式披露架构"
  
  deprecation_policy:
    notice_period: "30 days"
    migration_guide: "provided in release notes"
```

---

**版本**: 1.0.0  
**创建日期**: 2026-03-28  
**维护者**: emersonli  
**许可证**: MIT
