---
name: qa
version: 1.0.0
description: 智能测试专家 - Diff-aware 自动化测试生成和执行
domain: software-development
stage: 4-testing
input: 代码变更 + 测试计划（来自 /plan-eng-review）
output: QA 报告 + 健康度评分
nextSkill: ship
previousSkill: design-review
---

# 🧪 QA - 智能测试专家

## 🎯 核心价值

**测试不是为了证明代码正确，而是为了发现潜在问题。**

本技能专注于：
- ✅ Diff-aware 智能测试生成
- ✅ 浏览器自动化测试
- ✅ 视觉回归检测
- ✅ 健康度综合评分

---

## 📋 核心特性

### 1. Diff-Aware 测试

#### 代码变更分析

```yaml
diff_analysis:
  command: "git diff main...HEAD"
  
  affected_routes:
    from_controller_changes: |
      UserController.create → POST /users
      UserController.update → PATCH /users/:id
      
    from_view_changes: |
      users/show.html → GET /users/:id
      users/edit.html → GET /users/:id/edit
      
    from_model_changes: |
      User model → 所有用户相关页面
      
    from_css_changes: |
      global styles → 全站视觉回归
      
  test_generation_priority:
    1. "changed routes first"
    2. "critical paths (支付、登录)"
    3. "regression tests for previously broken"
    
  coverage_goal: "100% of changed code"
```

#### 智能测试生成

```typescript
// 基于 diff 自动生成测试
async function generateTestsFromDiff(diff: CodeDiff): Promise<TestSuite[]> {
  const tests: TestSuite[] = [];
  
  // 新增 API 端点 → 生成 API 测试
  if (diff.hasNewRoute()) {
    tests.push({
      type: 'api',
      route: diff.newRoute,
      tests: [
        { name: '200 OK with valid input', priority: 'high' },
        { name: '400 Bad Request with invalid input', priority: 'high' },
        { name: '401 Unauthorized without auth', priority: 'medium' }
      ]
    });
  }
  
  // 修改数据库模型 → 生成数据层测试
  if (diff.hasModelChanges()) {
    tests.push({
      type: 'integration',
      focus: 'database operations',
      tests: [
        { name: 'CRUD operations', priority: 'high' },
        { name: 'Validation rules', priority: 'high' },
        { name: 'Relationships', priority: 'medium' }
      ]
    });
  }
  
  // CSS 变更 → 生成视觉回归测试
  if (diff.hasCssChanges()) {
    tests.push({
      type: 'visual',
      pages: diff.affectedPages,
      baseline: 'main',
      threshold: 0.05 // 5% 差异阈值
    });
  }
  
  return tests;
}
```

---

### 2. 浏览器自动化

#### 使用 $B 工具

```yaml
browser_automation:
  tool: "$B (browse binary)"
  
  setup:
    import_cookies: |
      # 从真实浏览器导入登录态
      $B cookies import --profile=default
      
    set_viewport: |
      $B viewport set 1920x1080
      $B viewport add 768x1024  # iPad
      $B viewport add 375x667   # iPhone SE
  
  commands:
    navigation:
      - "$B goto http://localhost:3000"
      - "$B wait-for-selector '#app'"
      
    interaction:
      - "$B click '#login-btn'"
      - "$B type '#email' 'test@example.com'"
      - "$B type '#password' 'SecurePass123!'"
      - "$B submit-form '#login-form'"
      
    assertion:
      - "$B assert-visible '#welcome-message'"
      - "$B assert-text '#user-name' '包含：测试用户'"
      - "$B assert-url '/dashboard'"
      
    screenshot:
      - "$B screenshot initial.png"
      - "$B screenshot after-action.png --full-page"
      
    console_capture:
      - "$B console --errors > console-errors.log"
      - "$B console --warnings > console-warnings.log"
      
    network_monitoring:
      - "$B network --failed > failed-requests.log"
      - "$B network --slow > slow-requests.log"
```

#### 视觉回归对比

```yaml
visual_regression:
  baseline: "screenshots/baseline/"
  current: "screenshots/current/"
  diff: "screenshots/diff/"
  
  comparison:
    tool: "pixelmatch"
    threshold: 0.05  # 5% 像素差异容忍
    min_box_size: 10 # 忽略小于 10px 的差异
    
  output: |
    ## 视觉回归报告
    
    ### 通过的页面 (45)
    - ✅ / (0.02% 差异)
    - ✅ /products (0.03% 差异)
    
    ### 有差异的页面 (3)
    - ⚠️ /checkout (8.5% 差异)
      ![差异图](diff/checkout.png)
      主要变化：按钮位置调整
      
    - ❌ /profile (15.2% 差异) - 非预期
      ![差异图](diff/profile.png)
      问题：表单布局错乱
```

---

### 3. 测试执行策略

#### 并行测试执行

```yaml
parallel_execution:
  lanes:
    - name: "unit-tests"
      command: "npm run test:unit"
      timeout: "10m"
      parallel: true  # Jest 内部并行
      
    - name: "integration-tests"
      command: "npm run test:integration"
      timeout: "20m"
      services:
        - postgres:14
        - redis:7
        
    - name: "e2e-tests"
      command: "npm run test:e2e"
      timeout: "30m"
      browsers:
        - chromium
        - firefox
        - webkit
        
  failure_handling:
    retry_count: 2
    retry_delay: "5s"
    quarantine_flaky: true
```

#### 失败分类和修复

```yaml
failure_triage:
  categories:
    in_branch_failure: |
      定义：当前分支引入的新失败
      行动：阻塞发布，必须修复
      优先级：P0
      
    pre_existing_failure: |
      定义：主分支已存在的失败
      行动：记录并分配修复
      优先级：P1
      
    flaky_test: |
      定义：间歇性失败 (<80% 重现率)
      行动：隔离并标记，安排调查
      优先级：P2
      
    environment_failure: |
      定义：环境/基础设施问题
      行动：修复环境后重试
      优先级：P0
      
  auto_classification: |
    algorithm:
      1. 检查失败是否在 git diff 影响范围内
         - 是 → in_branch_failure
         - 否 → 检查主分支状态
           
      2. 对比主分支测试结果
         - 主分支也失败 → pre_existing_failure
         - 主分支通过 → in_branch_failure
           
      3. 重试 3 次检查稳定性
         - 通过率 <80% → flaky_test
         - 全部失败 → 确认失败
```

---

### 4. QA 报告生成

**输出文件**: `qa-report-{project-name}-{date}.md`

**报告结构**:

```markdown
# QA 报告

**项目名称**: {项目名称}  
**测试日期**: {YYYY-MM-DD}  
**Git 分支**: {branch-name}  
**Commit Range**: main...{commit-hash}

---

## 一、健康度评分

### 总体评分：**87/100** 🟢

| 维度 | 得分 | 权重 | 加权分 |
|------|------|------|--------|
| 测试覆盖率 | 92% | 25% | 23.0 |
| 测试通过率 | 98% | 25% | 24.5 |
| 代码质量 | 85% | 25% | 21.3 |
| 性能表现 | 88% | 15% | 13.2 |
| 安全性 | 90% | 10% | 9.0 |

### 评级说明
- **≥90**: 🟢 Excellent - 可直接发布
- **≥75**: 🟡 Good - 修复关键问题后发布
- **≥60**: 🟠 Needs Work - 需要改进
- **<60**: 🔴 Critical - 禁止发布

---

## 二、测试执行摘要

### 总览
- **运行测试数**: 1,245
- **通过**: 1,220 (98.0%)
- **失败**: 20 (1.6%)
- **跳过**: 5 (0.4%)
- **执行时间**: 12m 34s

### 按类型分布
| 类型 | 总数 | 通过 | 失败 | 通过率 |
|------|------|------|------|--------|
| 单元测试 | 856 | 850 | 6 | 99.3% |
| 集成测试 | 234 | 228 | 6 | 97.4% |
| E2E 测试 | 155 | 142 | 13 | 91.6% |

---

## 三、失败分析

### In-Branch Failures (新引入，必须修复)

#### ❌ 失败 #1: 用户注册流程 - 邮箱验证失败
- **测试**: `e2e/tests/auth/register.spec.ts:45`
- **错误**: `Expected element to be visible, but got hidden`
- **影响**: 新用户无法完成注册
- **根因**: 邮件服务 mock 配置错误
- **修复**: 
  ```diff
  - mockMailer.send.mockResolvedValue(false);
  + mockMailer.send.mockResolvedValue(true);
  ```
- **状态**: 🔧 修复中

#### ❌ 失败 #2: 购物车金额计算错误
- **测试**: `unit/tests/cart/calculations.test.ts:78`
- **错误**: `Expected: 99.99, Received: 109.99`
- **影响**: 订单金额计算错误
- **根因**: 税费计算逻辑遗漏折扣
- **状态**: ⏳ 待修复

---

### Pre-existing Failures (历史遗留)

#### ⚠️ 失败 #3-8: 移动端兼容性问题
- **影响**: Safari 浏览器部分功能异常
- **行动**: 已创建 JIRA TICKET: FE-1234
- **负责人**: @frontend-team
- **计划**: v1.3.0 修复

---

### Flaky Tests (不稳定测试)

#### 🔶 Flaky #1: API 响应时间测试
- **测试**: `perf/tests/api-response-time.spec.ts`
- **通过率**: 75% (3/4 次运行失败)
- **行动**: 隔离到 `tests/flaky/` 目录
- **调查**: 可能与测试环境负载有关

---

## 四、覆盖率分析

### 整体覆盖率

```
-------------------|---------|----------|---------|---------|-------------------
File               | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s 
-------------------|---------|----------|---------|---------|-------------------
All files          |   84.23 |    76.45 |   88.91 |   85.12 |                   
 src/              |         |          |         |         |                   
  api/             |   92.34 |    85.67 |   95.23 |   93.12 |                   
  components/      |   78.45 |    68.90 |   82.34 |   79.23 | 45,67,89,123      
  services/        |   88.90 |    79.45 |   91.23 |   89.45 |                   
  utils/           |   95.67 |    88.90 |   97.45 |   96.12 |                   
-------------------|---------|----------|---------|---------|-------------------
```

### 未覆盖的关键代码

#### 高风险未覆盖区域
1. `src/services/payment.ts:145-167` - 退款处理逻辑
2. `src/api/middleware.ts:34-56` - 认证中间件
3. `src/utils/validation.ts:78-92` - 输入验证

**建议**: 这些是关键路径，需要在发布前补充测试。

---

## 五、性能测试

### 关键指标

| 指标 | 当前值 | 目标值 | 状态 |
|------|--------|--------|------|
| 首页加载时间 | 1.2s | <1.5s | ✅ |
| API P95 延迟 | 180ms | <200ms | ✅ |
| LCP | 2.1s | <2.5s | ✅ |
| FID | 85ms | <100ms | ✅ |
| CLS | 0.08 | <0.1 | ✅ |

### 负载测试结果

```
Scenario: 100 并发用户
Duration: 5 minutes

Results:
  ✓ Throughput: 523 req/s (target: >500)
  ✓ P95 Latency: 198ms (target: <200ms)
  ✓ Error Rate: 0.3% (target: <1%)
  ✗ CPU Usage: 92% (target: <85%)

瓶颈识别:
  - 数据库查询在高峰期变慢
  - 建议：添加查询缓存或索引优化
```

---

## 六、安全问题

### 扫描结果

| 类别 | 发现问题 | 严重等级 |
|------|----------|----------|
| SQL 注入风险 | 0 | - |
| XSS 漏洞 | 1 | Medium |
| CSRF 保护 | 已启用 | ✅ |
| 敏感数据泄露 | 0 | - |
| 依赖安全漏洞 | 2 | Low |

### 需要修复的问题

#### ⚠️ Medium: XSS 风险
- **位置**: `src/components/Comment.tsx:34`
- **问题**: 用户输入未转义直接渲染
- **修复**: 
  ```diff
  - <div dangerouslySetInnerHTML={{ __html: content }} />
  + <div>{sanitize(content)}</div>
  ```

---

## 七、发布建议

### ✅ 推荐发布条件
- [x] 无 Critical 级别失败
- [x] 所有 In-Branch 失败已修复
- [x] 覆盖率 ≥60% (当前：84%)
- [x] 性能指标达标
- [x] 安全检查通过

### ⚠️ 已知问题
- 3 个 Pre-existing 失败（不影响发布）
- 1 个 Flaky 测试已隔离

### 🎯 发布决策

**结论**: ✅ **批准发布**

**条件**: 
- 无附加条件
- 可在下一个工作窗口发布

---

## 八、附录

### 测试 artefacts
- [详细测试日志](artifacts/test-run-log.txt)
- [覆盖率报告 HTML](artifacts/coverage/index.html)
- [性能测试报告](artifacts/perf-report.md)
- [截图对比](screenshots/)

### 命令记录
```bash
# 测试执行命令
npm test -- --ci --coverage
npm run test:e2e -- --browser=all
npm run perf:test
```

---

**审批**:
- [ ] QA 负责人：__________ 日期：__________
- [ ] Tech Lead: __________ 日期：__________
- [ ] Product Owner: ______ 日期：__________
```

---

## 🔧 工具调用规范

### Bash
用于执行测试和分析。

```yaml
tool: Bash
parameters:
  command: |
    # Diff 分析
    git diff main...HEAD --stat
    
    # 运行测试
    npm test -- --ci --coverage --reporters=default --reporters=jest-junit
    
    # 浏览器自动化
    $B goto http://localhost:3000/login
    $B screenshot login-page.png
```

### Write
用于保存 QA 报告。

```yaml
tool: Write
parameters:
  file_path: "/Users/lihao/.qoderwork/workspace/mnagcxtml4a9p1vc/team-orchestrator/qa-reports/qa-report-{name}-{date}.md"
  content: "{完整的 markdown 内容}"
```

---

## 📊 健康度评分算法

```python
def calculate_health_score(test_results):
    weights = {
        'coverage': 0.25,
        'pass_rate': 0.25,
        'code_quality': 0.20,
        'performance': 0.15,
        'security': 0.15
    }
    
    scores = {
        'coverage': min(100, test_results.coverage_percent),
        'pass_rate': test_results.pass_rate * 100,
        'code_quality': analyze_code_quality(),
        'performance': performance_score(),
        'security': security_scan_score()
    }
    
    total = sum(scores[k] * weights[k] for k in weights)
    
    return {
        'score': round(total, 1),
        'rating': get_rating(total),
        'breakdown': scores
    }

def get_rating(score):
    if score >= 90: return '🟢 Excellent'
    elif score >= 75: return '🟡 Good'
    elif score >= 60: return '🟠 Needs Work'
    else: return '🔴 Critical'
```

---

## 🚨 发布门禁

```yaml
release_gates:
  mandatory:
    - condition: "in_branch_failures == 0"
      action: "block if not met"
      
    - condition: "coverage >= 60%"
      action: "warn if <60%, block if <40%"
      
    - condition: "no_critical_security_issues"
      action: "block if not met"
      
  recommended:
    - condition: "coverage >= 80%"
      action: "encourage but allow override"
      
    - condition: "performance_metrics_met"
      action: "warn if not met"
      
  override_process:
    requires_approval_from:
      - "Tech Lead"
      - "QA Lead"
    reason_required: true
    documentation: "必须记录在 TODOS.md"
```

---

**版本**: 1.0.0  
**创建日期**: 2026-03-30  
**行业参考**: 业界最佳实践  
**维护者**: emersonli
