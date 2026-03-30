# 软件研发领域深度技能配置

> 受 gstack 启发，为应用研发团队添加完整的研发生命周期管理

## 🎯 核心价值主张

传统的团队配置只告诉你"需要多少人"，我们新增：
- ✅ **完整的研发流程**：从问题定义到发布上线
- ✅ **阶段化的技能**：每个阶段有专门的 AI 技能
- ✅ **自动化测试**：diff-aware 智能测试生成
- ✅ **安全门禁**：发布前的自动化检查
- ✅ **文档自动生成**：设计文档、测试计划、发布说明

---

## 📋 研发生命周期

```
┌──────────────┐
│ 1. Office    │
│    Hours     │ → 问题重构和需求验证
└──────┬───────┘
       ↓
┌──────────────┐
│ 2. Plan      │
│    Eng       │ → 架构设计和评审
│    Review    │
└──────┬───────┘
       ↓
┌──────────────┐
│ 3. Design    │
│    Review    │ → UI/UX审计和优化
└──────┬───────┘
       ↓
┌──────────────┐
│ 4. Build     │
│    (实施)    │ → 编码实现
└──────┬───────┘
       ↓
┌──────────────┐
│ 5. QA        │ → diff-aware 测试
└──────┬───────┘
       ↓
┌──────────────┐
│ 6. Ship      │
│    Release   │ → 自动化发布
└──────────────┘
```

---

## 🔧 六大核心技能

### 1. /office-hours - 问题重构专家

**目的**: 在写代码之前，确保解决的是正确的问题

**触发时机**: 
- 新功能创意
- 产品方向讨论
- 需求模糊不清时

**工作流程**:

#### Step 1: 模式选择
```yaml
AskUserQuestion:
  question: "这次讨论的目标是什么？"
  options:
    - Startup: "验证商业想法，找到最小可行方案"
    - Builder: "快速实现功能，学习或黑客松"
```

#### Step 2: 深度提问（Startup 模式）

**6 个强制问题**:
1. **Demand Reality**: "有什么证据表明用户真的需要这个？他们现在怎么解决这个问题？"
2. **Status Quo**: "现有的解决方案为什么不够好？用户愿意为什么付费？"
3. **Desperate Specificity**: "具体是谁会用？在什么场景下？多久用一次？"
4. **Narrowest Wedge**: "最小的可用版本是什么？砍掉哪些功能还能用？"
5. **Observation**: "你观察到用户的什么行为让你觉得这个很重要？"
6. **Future-Fit**: "如果成功了，1 年后这个产品会是什么样子？"

#### Step 3: 生成设计方案

**输出文档结构**:
```markdown
# 设计方案：[产品名称]

## 问题陈述
[清晰描述要解决的问题]

## 需求证据
- [ ] 用户访谈记录
- [ ] 现有解决方案分析
- [ ] 市场规模估算

## 目标用户
- 主要用户画像
- 使用场景
- 使用频率

## 假设验证
- 核心假设列表
- 验证方法
- 失败标准

## 考虑的方案
### 方案 A: 最小可行
- 功能列表
- 开发成本
- 风险

### 方案 B: 理想版本
- 功能列表
- 开发成本
- 风险

### 方案 C: 创新方案
- 功能列表
- 开发成本
- 风险

## 推荐方案
[详细说明为什么选择这个方案]

## 分发计划
- 如何获取第一批用户
- 增长策略
- 关键指标

## The Assignment
[明确的下一步行动和负责人]
```

#### Step 4: 对抗性评审

启动子代理循环：
```yaml
adversarial_review:
  rounds: 3
  perspectives:
    - "怀疑的用户": "这个真的有用吗？我为什么要用？"
    - "挑剔的工程师": "技术可行性如何？有什么风险？"
    - "精明的投资人": "商业模式是什么？规模有多大？"
  
  output: "修订后的设计方案 + 待解决问题清单"
```

---

### 2. /plan-eng-review - 架构设计专家

**目的**: 锁定架构、数据流、技术方案

**触发时机**:
- 开始实施前
- 重大重构前
- 技术方案不明确时

**工作流程**:

#### Step 0: 范围挑战

```yaml
checks:
  existing_code_reuse: "有没有现有代码可以复用？"
  minimum_changes: "最少需要改几个文件？"
  complexity_smell: ">8 个文件或 >2 个新类 → 需要重新思考"
```

#### Step 1: 架构图绘制

**生成 ASCII 数据流图**:
```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│   Client    │ ───→ │   API Gateway │ ───→ │   Service   │
│   (React)   │ ←─── │   (Kong)     │ ←─── │   (Node)    │
└─────────────┘      └──────────────┘      └──────┬──────┘
                                                   ↓
                                            ┌─────────────┐
                                            │  Database   │
                                            │  (Postgres) │
                                            └─────────────┘
```

**测试覆盖图**:
```
用户流程：登录 → 浏览 → 加购 → 支付
          ★★★    ★★☆    ★★★    ★★☆
          
★★★ = 100% 覆盖 + 边界测试
★★☆ = 主要路径覆盖
★☆☆ = 仅有冒烟测试
```

#### Step 2: 架构验证清单

```yaml
architecture_checklist:
  system_design:
    - [ ] 组件划分合理
    - [ ] 接口定义清晰
    - [ ] 数据流可追踪
    
  dependencies:
    - [ ] 评估了新依赖的必要性
    - [ ] 检查了许可证兼容性
    - [ ] 考虑了替代方案
    
  single_point_of_failure:
    - [ ] 识别了 SPOF
    - [ ] 有降级方案
    - [ ] 监控告警就绪
    
  security:
    - [ ] 认证授权机制
    - [ ] 输入验证
    - [ ] 敏感数据加密
    
  distribution:
    - [ ] 部署流程明确
    - [ ] 回滚方案就绪
    - [ ] 监控指标定义
```

#### Step 3: 故障模式分析

对每个代码路径分析：
```yaml
failure_modes:
  timeout: "如果这个调用超时怎么办？"
  nil_reference: "如果这个值是 null 怎么办？"
  race_condition: "如果有并发请求怎么办？"
  network_error: "如果网络失败怎么办？"
  disk_full: "如果磁盘满了怎么办？"
  
output: "故障处理矩阵 + 容错代码模板"
```

#### Step 4: 生成测试计划

**输出文件**: `~/.gstack/projects/{slug}/{user}-{branch}-eng-review-test-plan.md`

```markdown
# 测试计划

## 单元测试
- [ ] 所有新函数有单元测试
- [ ] 边界条件测试
- [ ] 错误处理测试

## 集成测试
- [ ] API 端点测试
- [ ] 数据库操作测试
- [ ] 外部服务 mock 测试

## E2E 测试
- [ ] 主要用户流程
- [ ] 关键路径覆盖
- [ ] 回归测试用例

## 性能测试
- [ ] 负载测试
- [ ] 压力测试
- [ ] 内存泄漏检测

## 覆盖率目标
- 行覆盖率：≥80%
- 分支覆盖率：≥70%
- 关键模块：100%
```

#### Step 5: 并行化策略

```yaml
parallelization:
  lanes:
    - name: "frontend"
      files: ["src/components/*", "src/pages/*"]
      dependencies: []
      
    - name: "backend-api"
      files: ["src/api/*", "src/models/*"]
      dependencies: []
      
    - name: "backend-workers"
      files: ["src/workers/*"]
      dependencies: ["backend-api"]
      
  execution: "worktree 并行执行"
```

---

### 3. /design-review - UI/UX 审计专家

**目的**: 80 项视觉和体验审计

**触发时机**:
- 设计稿完成后
- 前端开发完成后
- 上线前的 UI 走查

**工作流程**:

#### Step 1: 80 项审计清单

**视觉设计** (20 项):
```yaml
visual_design:
  - typography: "字体层级清晰？字号合适？"
  - color: "配色一致？对比度足够？"
  - spacing: "间距统一？对齐准确？"
  - imagery: "图片质量？图标风格一致？"
```

**交互设计** (25 项):
```yaml
interaction:
  - navigation: "导航清晰？面包屑？"
  - forms: "表单验证？错误提示？"
  - feedback: "加载状态？成功提示？"
  - gestures: "触摸目标大小？手势支持？"
```

**响应式** (15 项):
```yaml
responsive:
  - breakpoints: "各断点测试通过？"
  - mobile: "移动端体验良好？"
  - tablet: "平板适配？"
  - desktop: "大屏优化？"
```

**无障碍** (20 项):
```yaml
accessibility:
  - keyboard: "键盘可访问？"
  - screen_reader: "ARIA 标签？"
  - focus: "焦点管理？"
  - contrast: "对比度 WCAG AA？"
```

#### Step 2: 问题修复循环

```yaml
fix_loop:
  for_each_issue:
    - severity: "Critical / Major / Minor"
    - fix: "自动修复 or 手动修复"
    - verify: "截图对比 before/after"
    
  auto_fixable:
    - "对比度不足"
    - "触摸目标太小"
    - "缺少 alt 文本"
    - "表单无验证"
    
  manual_required:
    - "布局重构"
    - "交互逻辑调整"
    - "品牌色变更"
```

#### Step 3: 生成修复报告

```markdown
# Design Review 报告

## 总体评分：85/100

## Critical (必须修复)
- [x] 登录按钮对比度不足 4.5:1 → 已修复 ✓
- [ ] 表单无错误提示 → 待修复

## Major (建议修复)
- [x] 移动端导航菜单遮挡内容 → 已修复 ✓
- [ ] 加载状态缺失 → 待修复

## Minor (可选优化)
- [ ] 部分图标风格不一致
- [ ] 间距不统一

## Before/After 对比
![对比图](screenshots/issue-001-comparison.png)
```

---

### 4. /qa - 智能测试专家

**目的**: Diff-aware 自动化测试生成和执行

**触发时机**:
- 代码提交后
- PR 创建时
- 定期回归测试

**核心特性**:

#### Diff-Aware 测试

```yaml
diff_analysis:
  command: "git diff main...HEAD"
  
  affected_pages:
    - from_controller_changes: ["UserController → /users"]
    - from_view_changes: ["users/show.html → /users/:id"]
    - from_model_changes: ["User model → 所有用户相关页面"]
    - from_css_changes: ["global styles → 全站视觉回归"]
    
  test_generation:
    priority: "changed routes first"
    coverage_goal: "100% of changed code"
    regression: "all previously broken paths"
```

#### 浏览器自动化

```yaml
browser_automation:
  tool: "$B (browse binary)"
  
  commands:
    - navigate: "$B goto http://localhost:3000/users"
    - screenshot: "$B screenshot users-page.png"
    - console: "$B console --errors"
    - interact: "$B click '#login-btn'"
    - compare: "$B snapshot -D before after"
    
  cookie_import:
    from_real_browser: true
    for_auth_testing: true
```

#### 测试产物

```
.gstack/qa-reports/
├── qa-report-{domain}-{date}.md
├── screenshots/
│   ├── initial.png
│   ├── issue-001-step-1.png
│   ├── issue-001-after.png
│   └── ...
└── baseline.json

# 报告内容
- Health Score: 87/100
- Issues Found: 12
- Issues Fixed: 8
- Verification: ✓
```

---

### 5. /ship - 自动化发布专家

**目的**: 安全、自动化的发布流程

**触发时机**:
- 功能开发完成
- 测试全部通过
- 准备上线

**工作流程**:

#### Pre-flight 检查

```yaml
preflight_checks:
  branch_check: "不在主分支上？✓"
  git_status: "无未提交更改？✓"
  review_readiness: "Eng Review 完成？✓"
  merge_base: "合并主分支最新代码？✓"
```

#### 测试自动化

```yaml
test_execution:
  parallel_lanes:
    - frontend_tests: "npm test"
    - backend_tests: "bin/test-lane"
    
  failure_triage:
    in_branch_failure: "阻塞发布，必须修复"
    pre_existing_failure: "记录并分配修复"
    
  coverage_audit:
    minimum: "60%"
    target: "80%"
    gate: "<60% 阻塞发布（可 override）"
```

#### 版本号自动升级

```yaml
version_bump:
  rules:
    - diff_size < 100 lines: "MICRO bump (1.0.0 → 1.0.1)"
    - diff_size < 500 lines: "PATCH bump (1.0.0 → 1.1.0)"
    - breaking_changes: "MAJOR bump (1.0.0 → 2.0.0)"
    - new_features: "MINOR bump (1.0.0 → 1.1.0)"
    
  user_override: true
```

#### 发布说明自动生成

```yaml
changelog_generation:
  from_commits: "git log --oneline last_release..HEAD"
  
  grouping:
    - "🚀 Features"
    - "🐛 Bug Fixes"
    - "⚡ Performance"
    - "📚 Documentation"
    - "🧹 Chores"
    
  format: |
    ## [Version] - {date}
    
    ### 🚀 Features
    - Added user authentication (#123)
    - Implemented dark mode (#124)
    
    ### 🐛 Bug Fixes
    - Fixed login redirect issue (#125)
```

#### 安全门禁

```yaml
safety_gates:
  coverage_gate:
    condition: "coverage >= 60%"
    action: "block or override with reason"
    
  plan_audit:
    check: "所有 TODO 已完成 or 明确延期"
    action: "flag incomplete items"
    
  adversarial_review:
    diff_size < 50 lines: "skip"
    diff_size < 200 lines: "2-pass review"
    diff_size >= 200 lines: "4-pass full review"
    
  verification_gate:
    requirement: "fresh test run after any code change"
    action: "re-run tests if code changed"
```

#### 输出物

```yaml
deliverables:
  pr_mr:
    title: "[Release] v1.2.0 - User Authentication"
    body: |
      ## Summary
      - User authentication system
      - Dark mode support
      - Performance improvements
      
      ## Test Results
      - ✅ All tests passed (98% coverage)
      - ✅ Design review completed (92/100)
      - ✅ Security audit passed
      
      ## Review Findings
      - 3 minor issues fixed
      - 0 critical issues
      
      ## Commits
      - 12 commits from 3 authors
      
  version_file: "VERSION updated to 1.2.0"
  changelog: "CHANGELOG.md appended"
  todos: "TODOS.md updated"
```

---

## 🔗 技能间的协作

### 上下文链

```
/office-hours
  ↓ design_doc.md
/plan-eng-review
  ↓ test_plan.md + architecture_diagrams.md
/design-review  
  ↓ ui_audit_report.md
/build (实施)
  ↓ code changes
/qa
  ↓ qa_report.md + test_results
/ship
  ↓ release_notes.md + PR/MR
```

### 状态持久化

```yaml
state_storage:
  location: "~/.gstack/projects/{project_slug}/"
  
  artifacts:
    - design_docs/
    - eng_reviews/
    - design_audits/
    - qa_reports/
    - releases/
    
  history:
    - "每次运行的完整记录"
    - "决策和理由"
    - "问题和解决方案"
```

---

## 📊 度量指标

### 健康度评分

```yaml
health_score:
  dimensions:
    - code_quality: {weight: 0.25}
    - test_coverage: {weight: 0.25}
    - design_consistency: {weight: 0.15}
    - performance: {weight: 0.15}
    - security: {weight: 0.10}
    - documentation: {weight: 0.10}
    
  thresholds:
    excellent: "≥90"
    good: "≥75"
    needs_work: "≥60"
    critical: "<60"
```

### 流转效率

```yaml
flow_metrics:
  office_hours_to_plan: "平均 2 天"
  plan_to_build: "平均 1 天"
  build_to_qa: "平均 3 天"
  qa_to_ship: "平均 1 天"
  
  total_cycle_time: "平均 7 天"
  
  bottlenecks:
    - "Design Review 排队"
    - "QA 环境不稳定"
    - "发布审批慢"
```

---

## 🚀 实施路线图

### Phase 1: 基础框架 (v2.3.0)
- [ ] 定义 6 个技能的 SKILL.md
- [ ] 实现上下文链机制
- [ ] 创建状态存储结构

### Phase 2: 核心技能 (v2.4.0)
- [ ] 实现 /office-hours
- [ ] 实现 /plan-eng-review
- [ ] 实现 /qa

### Phase 3: 自动化 (v2.5.0)
- [ ] 实现 /design-review
- [ ] 实现 /ship
- [ ] 浏览器自动化集成

### Phase 4: 智能化 (v3.0.0)
- [ ] Diff-aware 测试生成
- [ ] 对抗性评审子代理
- [ ] 历史数据学习优化

---

**版本**: 1.0.0  
**创建日期**: 2026-03-28  
**维护者**: emersonli  
**灵感来源**: [gstack](https://github.com/garrytan/gstack)
