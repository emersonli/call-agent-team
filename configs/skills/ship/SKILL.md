---
name: ship
version: 1.0.0
description: 自动化发布专家 - 安全、自动化的发布流程
domain: software-development
stage: 5-release
input: 测试通过的代码 + QA 报告
output: PR/MR + 发布说明 + 版本标签
previousSkill: qa
---

# 🚀 Ship - 自动化发布专家

## 🎯 核心价值

**发布应该是无聊的、可预测的、安全的。**

本技能专注于：
- ✅ Pre-flight 自动化检查
- ✅ 并行测试执行和失败分类
- ✅ 版本号自动升级
- ✅ 发布说明自动生成
- ✅ 安全门禁和审批流

---

## 📋 工作流程

### Step 1: Pre-flight 检查

在开始发布流程前，进行系统性检查：

```yaml
preflight_checks:
  branch_validation:
    check: "不在主分支上"
    command: "git rev-parse --abbrev-ref HEAD"
    expected: "not main/master"
    action_if_fail: "中止：请在 feature 分支上操作"
    
  git_status:
    check: "无未提交更改"
    command: "git status --porcelain"
    expected: "empty output"
    action_if_fail: "提示：请提交或暂存所有更改"
    
  eng_review:
    check: "Eng Review 已完成"
    verify: "~/.gstack/projects/{slug}/eng-review-complete.md exists"
    action_if_fail: "请先运行 /plan-eng-review"
    
  merge_base:
    check: "合并主分支最新代码"
    command: "git merge-base main HEAD"
    recommendation: "建议先 rebase 到最新 main"
    
  qa_report:
    check: "QA 报告健康度 ≥60"
    verify: "qa-report-{date}.md health_score >= 60"
    action_if_fail: "请先修复关键问题"
```

---

### Step 2: 测试自动化

#### 并行测试执行

```yaml
test_execution:
  parallel_lanes:
    - name: "frontend-tests"
      command: "npm run test:unit -- --testPathPattern=src/"
      timeout: "15m"
      
    - name: "backend-tests"
      command: "bin/test-lane backend"
      timeout: "20m"
      services:
        - postgres
        - redis
        
    - name: "integration-tests"
      command: "npm run test:integration"
      timeout: "30m"
      
    - name: "e2e-critical"
      command: "npm run test:e2e -- --grep '@critical'"
      timeout: "45m"
      browsers: [chromium]
  
  failure_triage:
    in_branch_failure: |
      判定标准：失败在 git diff 影响范围内
      行动：阻塞发布，必须修复
      通知：@PR 作者
      
    pre_existing_failure: |
      判定标准：main 分支同样失败
      行动：记录并创建 JIRA ticket
      优先级：P1，不阻塞本次发布
      
    flaky_test: |
      判定标准：重试 3 次通过率 <80%
      行动：隔离到 flaky tests 目录
      调查：安排专人分析
      
  retry_strategy:
    max_retries: 2
    retry_delay: "5s"
    only_for: "timeout errors"
```

#### 覆盖率审计

```yaml
coverage_audit:
  thresholds:
    minimum: "60%"  # 门禁值
    target: "80%"   # 目标值
    excellent: "90%" # 优秀值
    
  enforcement:
    below_minimum: |
      action: "阻塞发布"
      override: "需要 Tech Lead + QA Lead 双重审批"
      
    below_target: |
      action: "警告，允许 override"
      recommendation: "记录技术债务"
      
  per_module_tracking:
    critical_modules:
      - path: "src/payment/"
        requirement: "≥90%"
      - path: "src/auth/"
        requirement: "≥85%"
        
    new_code_requirement: "≥80% (新代码更高要求)"
```

---

### Step 3: 版本号自动升级

#### 语义化版本规则

```yaml
semantic_versioning:
  format: "MAJOR.MINOR.PATCH (e.g., 1.2.3)"
  
  auto_bump_rules:
    patch_bump:
      conditions:
        - "diff_size < 100 lines"
        - "only bug fixes"
        - "no new features"
      example: "1.0.0 → 1.0.1"
      
    minor_bump:
      conditions:
        - "diff_size < 500 lines"
        - "new features added"
        - "backward compatible"
      example: "1.0.0 → 1.1.0"
      
    major_bump:
      conditions:
        - "breaking changes detected"
        - "diff_size >= 500 lines"
        - "API incompatible changes"
      example: "1.0.0 → 2.0.0"
      
  breaking_change_detection:
    indicators:
      - "API endpoint removed"
      - "request/response schema changed"
      - "database migration not backward compatible"
      - "authentication/authorization changed"
      
    commit_convention: |
      识别 BREAKING CHANGE 标记:
      - "BREAKING CHANGE:" in commit body
      - "!" after type: "feat!: remove API v1"
      - "major" label in PR
      
  user_override:
    allowed: true
    prompt: |
      当前变更分析：
      - 修改文件数：{N}
      - 新增行数：{N}
      - 删除行数：{N}
      - 检测到：{breaking/new/fix}
      
      推荐版本升级：{current} → {recommended}
      
      请选择：
      1) 按推荐升级 (回车确认)
      2) 手动指定版本 (major/minor/patch)
      3) 跳过版本升级
```

---

### Step 4: 发布说明自动生成

#### 从提交历史生成 Changelog

```yaml
changelog_generation:
  source: "git log --oneline last_release..HEAD"
  
  commit_parsing:
    conventional_commits: |
      格式：<type>(<scope>): <description>
      
      类型映射:
        feat → 🚀 Features
        fix → 🐛 Bug Fixes
        perf → ⚡ Performance
        docs → 📚 Documentation
        test → ✅ Tests
        refactor → 🔨 Refactoring
        chore → 🧹 Chores
        style → 💄 Styling
        ci → 👷 CI
        
  grouping_logic:
    primary_group: "commit type"
    secondary_group: "scope (optional)"
    sort_by: "importance then chronologically"
    
  pr_integration:
    fetch_pr_description: true
    extract_highlights: true
    include_screenshots: if_present
    
  format_template: |
    ## [Version {version}] - {release_date}
    
    ### 🚀 Features
    - Added user authentication system (#123) @emersonli
      - Support JWT token-based auth
      - Refresh token rotation
      - Session management
      
    - Implemented dark mode support (#124) @designerli
      ![Dark Mode Preview](screenshots/dark-mode.png)
    
    ### 🐛 Bug Fixes
    - Fixed login redirect issue when session expires (#125) @devwang
    - Resolved cart calculation error with discounts (#126) @coderkim
    
    ### ⚡ Performance
    - Optimized database queries, reduced latency by 40% (#127)
    - Implemented Redis caching for frequently accessed data (#128)
    
    ### 📚 Documentation
    - Updated API documentation with examples (#129)
    - Added deployment guide (#130)
    
    ### 🔨 Refactoring
    - Modularized payment service (#131)
    - Extracted shared utilities (#132)
    
    ### 👷 CI
    - Added automated release workflow (#133)
    - Improved test parallelization (#134)
    
    ---
    
    **Full Changelog**: [{previous_version}...{current_version}](link)
    
    **Contributors**: @emersonli, @designerli, @devwang, @coderkim (4)
    
    **Deployment**: 
    - Rollout: Canary 5% → 25% → 100%
    - Estimated time: 2 hours
```

---

### Step 5: 安全门禁

#### 多层安全检查

```yaml
safety_gates:
  gate_1_coverage:
    condition: "test_coverage >= 60%"
    action_on_fail: "block"
    override_requires:
      - "Tech Lead approval"
      - "Documented reason in TODOS.md"
      - "Plan to reach threshold in next sprint"
      
  gate_2_plan_audit:
    check: "所有 TODO 已完成 or 明确延期"
    verification: |
      - 检查 plan-eng-review 阶段的 TODO 列表
      - 确认每个 TODO 状态：Done or Deferred
      - Deferred 项目必须有明确责任人和日期
      
    action_on_fail: "flag incomplete items"
    
  gate_3_adversarial_review:
    rounds_based_on_diff_size:
      diff_size_lt_50: "skip"
      diff_size_lt_200: "2-pass review"
      diff_size_gte_200: "4-pass full review"
      
    perspectives:
      - "Security reviewer": 安全检查
      - "Performance reviewer": 性能影响
      - "Code quality reviewer": 代码质量
      - "User experience reviewer": 用户体验
      
    findings_resolution: |
      Critical: 必须修复后才能发布
      Major: 建议修复，允许 override
      Minor: 记录并安排后续修复
      
  gate_4_verification:
    requirement: "fresh test run after any code change"
    logic: |
      if code_changed_after_last_test:
        re_run_tests()
        
      if test_result_different:
        alert("Test result changed!")
        require_manual_approval()
        
  gate_5_rollback_readiness:
    checklist:
      - [ ] "回滚脚本已准备"
      - [ ] "数据库迁移可逆"
      - [ ] "监控告警已配置"
      - [ ] "on-call 人员已安排"
      
    verification_command: "bin/verify-rollback-ready"
```

---

### Step 6: 生成发布产物

#### PR/MR 自动生成

```yaml
pr_mr_generation:
  title_format: "[Release] v{version} - {highlight}"
  example: "[Release] v1.2.0 - User Authentication System"
  
  body_template: |
    ## 📋 Summary
    
    This release includes:
    - User authentication system with JWT
    - Dark mode support across all pages
    - Performance improvements (40% latency reduction)
    - 12 bug fixes
    
    ### Key Metrics
    - 📊 Test Coverage: 84% (+2% from last release)
    - ✅ Test Pass Rate: 98%
    - ⚡ Performance: All metrics met
    - 🔒 Security: No critical issues
    
    ---
    
    ## 🧪 Test Results
    
    | Type | Status | Details |
    |------|--------|---------|
    | Unit Tests | ✅ Pass | 856/856 |
    | Integration | ✅ Pass | 228/228 |
    | E2E | ✅ Pass | 142/142 |
    | Performance | ✅ Pass | All metrics met |
    
    **Health Score**: 87/100 🟢
    
    ---
    
    ## 📝 Review Findings
    
    ### Issues Found & Fixed
    - 3 minor UI inconsistencies (fixed)
    - 1 performance bottleneck (optimized)
    - 0 critical issues
    
    ### Known Limitations
    - Safari compatibility issues (tracked in FE-1234)
    - Flaky test isolated (test-utils.test.ts)
    
    ---
    
    ## 📦 Deployment Plan
    
    ### Rollout Strategy
    1. **Canary**: 5% users (30 min monitoring)
    2. **Early Access**: 25% users (1 hour monitoring)
    3. **General Availability**: 100% users
    
    ### Timeline
    - Start: {date} {time}
    - Complete: {date} {time}
    - Total Duration: ~2 hours
    
    ### Rollback Plan
    - Trigger: Error rate >2% or critical bug
    - Method: `bin/rollback-to {previous_version}`
    - ETA: <10 minutes
    
    ---
    
    ## 🔗 Related Links
    
    - Design Doc: [link]
    - Eng Review: [link]
    - QA Report: [link]
    - JIRA Epic: [link]
    
    ---
    
    ## ✅ Checklist
    
    - [x] Eng Review completed
    - [x] Design Review passed
    - [x] All tests passing
    - [x] Coverage requirements met
    - [x] Security scan passed
    - [x] Performance benchmarks met
    - [x] Rollback tested
    - [x] On-call scheduled
    
    /cc @tech-lead @qa-lead @product-owner
```

#### 版本文件更新

```yaml
version_files:
  VERSION:
    action: "update content"
    new_value: "{new_version}"
    
  package.json:
    action: "npm version {new_version} --no-git-tag-version"
    
  CHANGELOG.md:
    action: "prepend new section"
    location: "after header"
    
  TODOS.md:
    action: "update status"
    mark_completed: "items in this release"
    add_new: "follow-up tasks from review"
```

---

## 🔧 工具调用规范

### AskUserQuestion
用于版本升级决策。

```yaml
tool: AskUserQuestion
parameters:
  questions:
    - question: "版本升级策略？"
      header: "版本"
      multiSelect: false
      options:
        - label: "自动推荐 (Patch)"
          description: "1.0.0 → 1.0.1 - Bug 修复为主"
        - label: "Minor 升级"
          description: "1.0.0 → 1.1.0 - 新功能"
        - label: "Major 升级"
          description: "1.0.0 → 2.0.0 - 破坏性变更"
        - label: "手动指定"
          description: "自定义版本号"
```

### Bash
用于 Git 操作和自动化。

```yaml
tool: Bash
parameters:
  command: |
    # 版本升级
    npm version 1.2.0 --no-git-tag-version
    
    # 创建标签
    git tag -a "v1.2.0" -m "Release v1.2.0 - User Authentication"
    
    # 推送标签
    git push origin v1.2.0
    
    # 创建 PR (使用 gh CLI)
    gh pr create \
      --title "[Release] v1.2.0 - User Authentication" \
      --body-file .github/PULL_REQUEST_TEMPLATE.md \
      --base main \
      --label "release" \
      --reviewer "tech-lead,qa-lead"
```

---

## 📊 度量指标

### 发布健康度

```yaml
release_health_score:
  dimensions:
    test_quality: {weight: 0.30}  # 测试覆盖率和通过率
    code_quality: {weight: 0.25}  # 代码审查结果
    performance: {weight: 0.20}   # 性能指标
    security: {weight: 0.15}      # 安全扫描
    documentation: {weight: 0.10} # 文档完整性
    
  thresholds:
    excellent: "≥90 - 快速通道发布"
    good: "≥75 - 正常发布流程"
    needs_work: "≥60 - 需要额外审查"
    critical: "<60 - 禁止发布"
```

### 发布效率

```yaml
release_metrics:
  average_time_to_release: "从代码完成到上线的平均时间"
  target: "<4 hours"
  
  success_rate: "成功发布的比例"
  target: "≥95%"
  
  rollback_rate: "需要回滚的比例"
  target: "<5%"
  
  mean_time_to_recovery: "出问题时恢复的平均时间"
  target: "<10 minutes"
```

---

## 🚨 安全护栏

### 强制检查（不可绕过）
- ✅ 不在主分支上
- ✅ 无未提交更改
- ✅ 无 Critical 安全漏洞
- ✅ 覆盖率 ≥40% (绝对最低线)

### 可绕过的检查（需要审批）
- ⚠️ 覆盖率 <80% → Tech Lead 审批
- ⚠️ 已知非阻塞 Bug → Product Owner 审批
- ⚠️ 性能指标轻微超标 → 记录并监控

### 禁止行为
- ❌ 跳过所有测试直接发布
- ❌ 手动修改生产数据库无回滚方案
- ❌ 无审批绕过强制门禁

---

## 💡 最佳实践

### 发布清单
1. **提前准备**
   - 至少提前 1 小时开始发布流程
   - 确认 on-call 人员在岗
   - 检查监控 dashboard 正常

2. **渐进式发布**
   - 5% canary → 观察 30 分钟
   - 25% early access → 观察 1 小时
   - 100% GA → 持续监控

3. **快速回滚**
   - 自动化回滚脚本随时待命
   - 定义清晰的回滚触发条件
   - 定期演练回滚流程

### 常见陷阱
1. **周五发布**
   - 避免在周末前发布重大变更
   - 如必须发布，安排周末 on-call

2. **忽视监控**
   - 发布后至少监控 1 小时
   - 设置临时 dashboard 追踪关键指标

3. **沟通不足**
   - 提前通知客服和支持团队
   - 在状态页面发布公告
   - 准备好用户 FAQ

---

**版本**: 1.0.0  
**创建日期**: 2026-03-30  
**灵感来源**: [gstack /ship](https://github.com/garrytan/gstack)  
**维护者**: emersonli
