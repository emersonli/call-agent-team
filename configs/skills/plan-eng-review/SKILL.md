---
name: plan-eng-review
version: 1.0.0
description: 架构设计和评审专家 - 锁定技术方案、数据流、测试计划
domain: software-development
stage: 2-planning
input: 设计方案文档（来自 /office-hours）
output: 架构图 + 测试计划 + 故障模式分析
nextSkill: design-review
previousSkill: office-hours
---

# 📐 Plan-Eng-Review - 架构设计专家

## 🎯 核心价值

**优秀的架构设计让正确的实现变得容易。**

本技能专注于：
- ✅ 系统架构和数据流设计
- ✅ 技术选型和依赖评估
- ✅ 故障模式分析和容错设计
- ✅ 测试计划和覆盖率规划
- ✅ 并行化开发策略

---

## 📋 工作流程

### Step 0: 范围挑战和简化

在开始设计之前，先挑战范围：

```yaml
scope_challenge:
  questions:
    - "有没有现有代码可以复用？具体是哪些模块？"
    - "最少需要改几个文件？能否更少？"
    - "如果只能实现一个核心功能，是哪个？"
    
  warning_thresholds:
    files_changed: ">8 个文件 → 需要重新思考"
    new_classes: ">2 个新类 → 考虑简化"
    external_deps: ">3 个新依赖 → 评估必要性"
    
  simplification_prompt: |
    我注意到这个方案涉及 {N} 个文件/组件。让我们重新思考：
    
    1. 能否先用最简单的方式验证核心假设？
    2. 哪些功能可以延迟到下一阶段？
    3. 有没有现成的库或服务可以替代自建？
```

---

### Step 1: 架构图绘制

#### 1.1 生成 ASCII 数据流图

**模板**:

```
┌─────────────────┐      ┌──────────────────┐      ┌─────────────────┐
│   Client        │      │   API Gateway    │      │   Service       │
│   (React/Vue)   │ ───→ │   (Kong/Nginx)   │ ───→ │   (Node/Go)     │
│                 │ ←─── │                  │ ←─── │                 │
└─────────────────┘      └──────────────────┘      └────────┬────────┘
                                                            ↓
                                                     ┌─────────────────┐
                                                     │   Database      │
                                                     │   (Postgres)    │
                                                     └─────────────────┘
                                                             
辅助服务:
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│   Cache     │  │   Queue     │  │   Search    │
│   (Redis)   │  │   (Kafka)   │  │   (ES)      │
└─────────────┘  └─────────────┘  └─────────────┘
```

**生成规则**:
- 每个组件标注技术栈
- 箭头标注通信协议（HTTP/gRPC/WebSocket）
- 关键数据流用不同符号标记（═══ 表示同步，┄┄┄表示异步）

#### 1.2 测试覆盖图

**格式**:

```
用户流程：注册 → 登录 → 浏览 → 加购 → 支付 → 订单
          ★★☆    ★★★    ★★☆    ★★★    ★★☆    ★★☆
          
API 端点：POST  → GET   → GET   → POST  → POST  → GET
         /users   /auth   /items  /cart   /pay    /order

★★★ = 100% 覆盖 + 边界条件 + 错误处理
★★☆ = 主要路径覆盖 + 基本错误处理  
★☆☆ = 仅有冒烟测试
```

**生成逻辑**:
- 基于用户流程自动生成测试路径
- 为每个步骤推荐测试覆盖率等级
- 识别关键路径（支付、认证等）需要★★★

---

### Step 2: 架构验证清单

#### 2.1 系统设计维度

```yaml
system_design_checklist:
  component_design:
    - [ ] 组件划分是否合理？（单一职责）
    - [ ] 接口定义是否清晰？（输入输出明确）
    - [ ] 数据流是否可追踪？（从入口到存储）
    - [ ] 状态管理是否一致？（客户端/服务端）
    
  module_boundaries:
    - [ ] 模块间耦合度是否足够低？
    - [ ] 循环依赖是否避免？
    - [ ] 公共层是否合理抽象？
    - [ ] 领域层是否业务纯净？
```

#### 2.2 依赖评估维度

```yaml
dependencies_checklist:
  new_dependencies_review:
    - [ ] 为什么需要这个依赖？有替代方案吗？
    - [ ] 社区活跃度如何？（GitHub stars, npm downloads）
    - [ ] 最后更新时间是什么时候？
    - [ ] 许可证是否兼容？（MIT/Apache/GPL）
    - [ ] 是否有已知的安全问题？
    - [ ] 体积/性能影响是多少？
    
  third_party_services:
    - [ ] SLA 保障是多少？（99.9%? 99.99%?）
    - [ ] 定价模型是什么？（免费/按量/包月）
    - [ ] 数据导出是否方便？（避免 vendor lock-in）
    - [ ] 有无备选方案？（故障切换）
```

#### 2.3 单点故障维度

```yaml
spof_analysis:
  identification:
    - [ ] 数据库是否是单点？→ 主从复制？
    - [ ] 缓存是否是单点？→ 集群部署？
    - [ ] 消息队列是否是单点？→ 多 broker？
    - [ ] 外部 API 是否是单点？→ 降级方案？
    
  mitigation:
    - [ ] 每个 SPOF 的降级方案是什么？
    - [ ] 监控告警是否就绪？（指标 + 阈值）
    - [ ] 故障恢复流程是否文档化？
    - [ ] 是否进行过故障演练？
```

#### 2.4 安全维度

```yaml
security_checklist:
  authentication_authorization:
    - [ ] 用户认证机制？（JWT/OAuth2/Session）
    - [ ] 权限控制粒度？（RBAC/ABAC）
    - [ ] API 鉴权如何实现？
    - [ ] 敏感操作是否需要二次确认？
    
  input_validation:
    - [ ] 所有输入是否验证？（前端 + 后端）
    - [ ] SQL 注入防护？（参数化查询）
    - [ ] XSS 防护？（转义/CSP）
    - [ ] CSRF 防护？（token 验证）
    
  data_protection:
    - [ ] 敏感数据是否加密存储？（密码/个人信息）
    - [ ] 传输是否使用 HTTPS/TLS？
    - [ ] 密钥如何管理？（环境变量/密钥管理服务）
    - [ ] 日志是否脱敏？（不记录密码/信用卡号）
```

#### 2.5 部署运维维度

```yaml
devops_checklist:
  deployment:
    - [ ] 部署流程是否自动化？（CI/CD）
    - [ ] 回滚方案是否就绪？（一键回滚）
    - [ ] 环境配置是否分离？（dev/staging/prod）
    - [ ] 数据库迁移如何处理？（向后兼容）
    
  monitoring:
    - [ ] 关键指标是否监控？（QPS/延迟/错误率）
    - [ ] 日志是否集中收集？（ELK/Loki）
    - [ ] 告警阈值是否合理？（避免告警疲劳）
    - [ ] Dashboard 是否可视化？（Grafana）
    
  scalability:
    - [ ] 水平扩展能力？（无状态服务）
    - [ ] 数据库扩展策略？（分库分表/读写分离）
    - [ ] 缓存策略是否合理？（TTL/淘汰策略）
    - [ ] CDN 是否利用？（静态资源加速）
```

---

### Step 3: 故障模式分析

对每个关键代码路径进行系统性分析：

#### 3.1 故障场景清单

```yaml
failure_scenarios:
  network_related:
    - timeout: "如果这个 API 调用超时怎么办？"
    - connection_refused: "如果连接被拒绝怎么办？"
    - dns_failure: "如果 DNS 解析失败怎么办？"
    - ssl_error: "如果 SSL 证书验证失败怎么办？"
    
  resource_related:
    - disk_full: "如果磁盘满了怎么办？"
    - memory_exhausted: "如果内存耗尽怎么办？"
    - connection_pool_empty: "如果连接池耗尽怎么办？"
    - rate_limit_exceeded: "如果超过速率限制怎么办？"
    
  data_related:
    - nil_reference: "如果这个值是 null/undefined 怎么办？"
    - empty_result: "如果查询结果为空怎么办？"
    - duplicate_key: "如果违反唯一约束怎么办？"
    - foreign_key_violation: "如果外键约束失败怎么办？"
    
  concurrency_related:
    - race_condition: "如果有并发请求怎么办？"
    - deadlock: "如果发生死锁怎么办？"
    - stale_read: "如果读到旧数据怎么办？"
    - lost_update: "如果更新被覆盖怎么办？"
    
  external_service:
    - third_party_down: "如果第三方服务宕机怎么办？"
    - api_version_changed: "如果 API 版本不兼容怎么办？"
    - quota_exceeded: "如果用尽配额怎么办？"
    - response_malformed: "如果响应格式异常怎么办？"
```

#### 3.2 故障处理矩阵

**输出格式**:

```markdown
# 故障处理矩阵

## 模块：用户认证

| 故障场景 | 可能性 | 影响 | 处理策略 | 代码位置 |
|----------|--------|------|----------|----------|
| JWT 过期 | 高 | 中 | 刷新 token 或重定向登录 | `auth.middleware.ts:45` |
| 数据库连接失败 | 中 | 高 | 降级到缓存 session + 告警 | `auth.service.ts:78` |
| 密码哈希失败 | 低 | 高 | 返回友好错误 + 记录日志 | `auth.service.ts:32` |
| 暴力破解尝试 | 中 | 高 | 限流 + 临时封禁 + 通知 | `auth.middleware.ts:92` |

## 模块：支付处理

| 故障场景 | 可能性 | 影响 | 处理策略 | 代码位置 |
|----------|--------|------|----------|----------|
| 支付网关超时 | 中 | 高 | 重试 3 次 + 异步回调确认 | `payment.service.ts:156` |
| 余额不足 | 高 | 中 | 返回明确错误提示 | `payment.service.ts:89` |
| 重复支付 | 低 | 高 | 幂等性检查 + 自动退款 | `payment.service.ts:201` |
```

#### 3.3 容错代码模板

**示例模板**:

```typescript
// 带重试的 HTTP 调用
async function callWithRetry<T>(
  url: string,
  options: RequestInit,
  maxRetries: number = 3
): Promise<T> {
  let lastError: Error;
  
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const response = await fetch(url, {
        ...options,
        signal: AbortSignal.timeout(5000) // 5 秒超时
      });
      
      if (!response.ok) {
        throw new HttpError(`HTTP ${response.status}`, response);
      }
      
      return await response.json();
      
    } catch (error) {
      lastError = error as Error;
      
      // 指数退避：1s, 2s, 4s
      const delay = Math.pow(2, attempt - 1) * 1000;
      await sleep(delay);
    }
  }
  
  // 所有重试失败
  logger.error('All retries failed', { url, error: lastError });
  throw new ServiceUnavailableError('External service unavailable', lastError);
}

// 空值保护
function getUserDisplayName(user: User | null): string {
  return user?.profile?.displayName ?? 
         user?.email?.split('@')[0] ?? 
         '匿名用户';
}

// 幂等性保证
async function processPayment(paymentId: string, amount: number): Promise<void> {
  const key = `payment:${paymentId}`;
  
  // 使用分布式锁防止重复处理
  const lock = await redis.acquireLock(key, 30000);
  if (!lock) {
    logger.warn('Duplicate payment request', { paymentId });
    return; // 已经在处理中
  }
  
  try {
    // 检查是否已经处理过
    const existing = await db.payment.findUnique({ where: { id: paymentId } });
    if (existing?.status === 'COMPLETED') {
      return; // 幂等返回
    }
    
    // 实际处理逻辑
    await gateway.charge(amount);
    await db.payment.update({ where: { id: paymentId }, data: { status: 'COMPLETED' } });
    
  } finally {
    await lock.release();
  }
}
```

---

### Step 4: 生成测试计划

**输出文件**: `test-plan-{project-name}-{date}.md`

**完整模板**:

```markdown
# 测试计划

**项目名称**: {项目名称}  
**创建日期**: {YYYY-MM-DD}  
**架构评审版本**: v1.0  
**关联设计文档**: [design-doc-{name}.md](../design-docs/design-doc-{name}.md)

---

## 一、测试策略概述

### 测试金字塔

```
        /\
       /  \
      / E2E \      10% - 关键用户流程
     /______\
    /        \
   /Integration\   30% - 组件集成/API 测试
  /______________\
 /  Unit Tests    \ 60% - 单元测试
/__________________\
```

### 测试重点
- **核心业务逻辑**: 100% 覆盖
- **用户界面**: 主要交互流程
- **外部集成**: Mock + 契约测试
- **性能关键路径**: 负载测试 + 压力测试

---

## 二、单元测试

### 2.1 新函数覆盖

#### 模块：用户认证 (`auth.service.ts`)

| 函数名 | 测试用例 | 优先级 |
|--------|----------|--------|
| `validatePassword()` | - 有效密码 ✓<br>- 长度不足 ✗<br>- 缺少特殊字符 ✗<br>- 常见密码 ✗ | High |
| `generateJwtToken()` | - 正常生成 ✓<br>- 过期时间正确 ✓<br>- payload 完整 ✓ | High |
| `verifyJwtToken()` | - 有效 token ✓<br>- 过期 token ✗<br>- 篡改 token ✗<br>- 签发者不匹配 ✗ | High |

#### 模块：支付处理 (`payment.service.ts`)

| 函数名 | 测试用例 | 优先级 |
|--------|----------|--------|
| `calculateTotal()` | - 正常计算 ✓<br>- 折扣应用 ✓<br>- 税费计算 ✓<br>- 边界值 (0, 负数) ✗ | High |
| `processRefund()` | - 全额退款 ✓<br>- 部分退款 ✓<br>- 重复退款 ✗<br>- 余额不足 ✗ | High |

### 2.2 边界条件测试

```typescript
describe('边界条件测试', () => {
  it('处理空数组', () => {
    expect(calculateTotal([])).toBe(0);
  });
  
  it('处理极大数值', () => {
    const largeNumber = Number.MAX_SAFE_INTEGER;
    expect(() => calculateTotal([largeNumber])).not.toThrow();
  });
  
  it('处理浮点数精度', () => {
    expect(calculateTotal([0.1, 0.2])).toBeCloseTo(0.3, 2);
  });
  
  it('处理负数输入', () => {
    expect(() => createOrder(-100)).toThrow('InvalidAmountError');
  });
});
```

### 2.3 错误处理测试

```typescript
describe('错误处理测试', () => {
  it('网络超时时抛出正确错误', async () => {
    mockFetch.mockRejectedValue(new TimeoutError());
    
    await expect(processPayment('123', 100))
      .rejects
      .toThrow(ServiceUnavailableError);
  });
  
  it('数据库连接失败时降级', async () => {
    mockDb.query.mockRejectedValue(new ConnectionError());
    
    const result = await getUserProfile('user-123');
    expect(result).toBeNull(); // 降级返回 null
    expect(mockCache.get).toHaveBeenCalledWith('user:user-123');
  });
});
```

---

## 三、集成测试

### 3.1 API 端点测试

#### 用户相关端点

```yaml
GET /api/users/:id:
  status: 200
  response:
    id: string
    email: string
    displayName: string
    
  status: 404
  response:
    error: "User not found"
    
  status: 401
  response:
    error: "Unauthorized"

POST /api/users:
  status: 201
  request:
    email: string
    password: string
  response:
    id: string
    token: string
    
  status: 400
  response:
    errors:
      - field: "email"
        message: "Invalid email format"
```

### 3.2 数据库操作测试

```typescript
describe('UserRepository', () => {
  beforeAll(async () => {
    await db.migrate.up(); // 运行迁移
  });
  
  afterAll(async () => {
    await db.migrate.down(); // 清理
  });
  
  it('创建用户并查询', async () => {
    const user = await userRepository.create({
      email: 'test@example.com',
      password: 'secure123'
    });
    
    const found = await userRepository.findById(user.id);
    expect(found.email).toBe('test@example.com');
  });
  
  it('事务回滚测试', async () => {
    await expect(
      db.transaction(async (tx) => {
        await tx.user.create({ data: { email: 'a@b.com' } });
        throw new Error('Rollback');
      })
    ).rejects.toThrow('Rollback');
    
    const count = await db.user.count();
    expect(count).toBe(0); // 确保回滚
  });
});
```

### 3.3 外部服务 Mock 测试

```typescript
describe('PaymentService with mocked gateway', () => {
  let mockGateway: jest.Mocked<PaymentGateway>;
  
  beforeEach(() => {
    mockGateway = {
      charge: jest.fn(),
      refund: jest.fn(),
      getStatus: jest.fn()
    };
  });
  
  it('支付成功时更新订单状态', async () => {
    mockGateway.charge.mockResolvedValue({ success: true, transactionId: 'txn_123' });
    
    await paymentService.process('order-456', 9900);
    
    expect(mockGateway.charge).toHaveBeenCalledWith(9900);
    expect(mockOrder.update).toHaveBeenCalledWith(
      { id: 'order-456' },
      { status: 'PAID', transactionId: 'txn_123' }
    );
  });
  
  it('支付失败时发送通知', async () => {
    mockGateway.charge.mockRejectedValue(new GatewayError('Declined'));
    
    await paymentService.process('order-789', 5000);
    
    expect(mockNotification.send).toHaveBeenCalledWith(
      'order-789',
      '支付失败，请重试'
    );
  });
});
```

---

## 四、E2E 测试

### 4.1 主要用户流程

#### 流程：用户注册 → 登录 → 浏览 → 下单

```gherkin
Feature: 用户购物流程
  
  Scenario: 新用户完成首次购买
    Given 我访问首页
    When 我点击"注册"按钮
    And 我填写有效的注册信息
    And 我提交表单
    Then 我应该看到欢迎消息
    
    When 我搜索商品"手机"
    And 我将第一个商品加入购物车
    And 我进入结算流程
    And 我选择配送地址和支付方式
    And 我确认订单
    Then 我应该看到订单确认页面
    And 我应该收到订单确认邮件
```

### 4.2 关键路径覆盖

**关键路径清单**:
1. ✅ 用户注册和登录
2. ✅ 商品搜索和筛选
3. ✅ 购物车操作（添加/修改/删除）
4. ✅ 订单创建和支付
5. ✅ 订单状态查询
6. ✅ 退款申请

### 4.3 回归测试用例

**历史 Bug 回归**:
- [ ] Bug #123: 购物车数量显示错误 → 已修复，添加回归测试
- [ ] Bug #456: 优惠券叠加使用 → 已修复，添加回归测试

---

## 五、性能测试

### 5.1 负载测试

```yaml
scenario: "100 并发用户浏览商品"
duration: 5 minutes
ramp_up: 30 seconds

endpoints:
  - path: GET /api/products
    target_rps: 100
    expected_p95_latency: <200ms
    
  - path: GET /api/products/:id
    target_rps: 200
    expected_p95_latency: <100ms
    
success_criteria:
  - error_rate: <1%
  - p95_latency: <500ms
  - throughput: >500 req/s
```

### 5.2 压力测试

```yaml
scenario: "逐步增加负载直到系统崩溃"
duration: 30 minutes

load_pattern:
  start_users: 10
  increment: 10
  interval: 1 minute
  max_users: 1000
  
breakpoint_detection:
  - error_rate > 5%
  - p95_latency > 2000ms
  - cpu_usage > 90%
  - memory_usage > 85%
```

### 5.3 内存泄漏检测

```javascript
// 使用 Node.js heap snapshot
describe('内存泄漏检测', () => {
  it('不应该有内存泄漏', async () => {
    const initialMemory = process.memoryUsage().heapUsed;
    
    // 执行 1000 次操作
    for (let i = 0; i < 1000; i++) {
      await userService.createUser({
        email: `test${i}@example.com`,
        password: 'secure123'
      });
    }
    
    const finalMemory = process.memoryUsage().heapUsed;
    const growth = ((finalMemory - initialMemory) / initialMemory) * 100;
    
    expect(growth).toBeLessThan(50); // 增长不超过 50%
  });
});
```

---

## 六、覆盖率目标

### 6.1 整体目标

| 指标 | 目标值 | 门禁值 |
|------|--------|--------|
| 行覆盖率 | ≥80% | ≥60% |
| 分支覆盖率 | ≥70% | ≥50% |
| 函数覆盖率 | ≥85% | ≥65% |
| 语句覆盖率 | ≥80% | ≥60% |

### 6.2 关键模块要求

**必须 100% 覆盖的模块**:
- [ ] 支付处理 (`payment/`)
- [ ] 用户认证 (`auth/`)
- [ ] 数据加密 (`crypto/`)
- [ ] 权限校验 (`authorization/`)

### 6.3 覆盖率报告配置

```json
{
  "coverage": {
    "reporter": ["text", "lcov", "html"],
    "watermarks": {
      "lines": [60, 80],
      "functions": [65, 85],
      "branches": [50, 70],
      "statements": [60, 80]
    },
    "thresholds": {
      "global": {
        "lines": 60,
        "functions": 65,
        "branches": 50,
        "statements": 60
      },
      "each": {
        "lines": 80,
        "functions": 85,
        "branches": 70,
        "statements": 80
      }
    }
  }
}
```

---

## 七、测试执行计划

### 7.1 CI/CD 集成

```yaml
# .github/workflows/test.yml
name: Test Suite

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm ci
      - run: npm run test:unit -- --coverage
      
  integration-tests:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:14
        env:
          POSTGRES_PASSWORD: test
    steps:
      - uses: actions/checkout@v3
      - run: npm ci
      - run: npm run test:integration
      
  e2e-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm ci
      - run: npm run test:e2e
```

### 7.2 本地测试命令

```bash
# 运行所有测试
npm test

# 仅运行单元测试
npm run test:unit

# 仅运行集成测试
npm run test:integration

# 仅运行 E2E 测试
npm run test:e2e

# 运行测试并生成覆盖率报告
npm test -- --coverage

# 运行失败的测试
npm test -- --onlyFailed

# 监视模式
npm test -- --watch
```

### 7.3 测试数据管理

```typescript
// test/fixtures/user-fixture.ts
export const userFixtures = {
  validUser: {
    email: 'valid@example.com',
    password: 'SecurePass123!',
    displayName: '测试用户'
  },
  
  invalidEmail: {
    email: 'invalid-email',
    password: 'SecurePass123!'
  },
  
  weakPassword: {
    email: 'user@example.com',
    password: '123456'
  }
};

// 每个测试后清理
afterEach(async () => {
  await db.user.deleteMany();
  await db.order.deleteMany();
});
```

---

## 八、附录

### 8.1 测试工具链

- **单元测试框架**: Jest / Vitest
- **E2E 测试**: Playwright / Cypress
- **API 测试**: Supertest
- **性能测试**: k6 / Artillery
- **Mock 服务**: MSW (Mock Service Worker)
- **测试数据**: Faker.js

### 8.2 参考资源

- [Jest 最佳实践](https://jestjs.io/docs/best-practices)
- [Testing Library 指南](https://testing-library.com/docs/)
- [Playwright 文档](https://playwright.dev/)

---

**审批**:
- [ ] 架构师审批：__________ 日期：__________
- [ ] Tech Lead 审批：__________ 日期：__________
- [ ] QA Lead 审批：__________ 日期：__________
```

---

### Step 5: 并行化策略

对于大型项目，推荐并行开发策略：

```yaml
parallelization_strategy:
  worktree_setup: |
    # 创建多个 worktree 并行开发
    git worktree add ../frontend-feature origin/frontend-feature
    git worktree add ../backend-api origin/backend-api
    git worktree add ../backend-workers origin/backend-workers
    
  lanes:
    - name: "frontend"
      focus: "UI 组件和页面"
      files:
        - "src/components/**"
        - "src/pages/**"
        - "src/hooks/**"
      dependencies: []
      estimated_duration: "3-5 天"
      
    - name: "backend-api"
      focus: "RESTful API 和业务逻辑"
      files:
        - "src/api/**"
        - "src/models/**"
        - "src/services/**"
      dependencies: []
      estimated_duration: "4-6 天"
      
    - name: "backend-workers"
      focus: "后台任务和批处理"
      files:
        - "src/workers/**"
        - "src/jobs/**"
      dependencies:
        - "backend-api"  # 依赖 API 的数据模型
      estimated_duration: "2-3 天"
      
  synchronization:
    daily_merge: "每天下班前合并到 develop 分支"
    conflict_resolution: "小步快跑，尽早解决冲突"
    integration_test: "每次合并后运行集成测试"
```

---

## 🔧 工具调用规范

### AskUserQuestion
用于范围挑战和简化决策。

```yaml
tool: AskUserQuestion
parameters:
  questions:
    - question: "这个功能能否简化？"
      header: "范围"
      multiSelect: false
      options:
        - label: "MVP 版本"
          description: "只做核心功能，快速验证"
        - label: "完整版本"
          description: "包含所有规划的功能"
        - label: "分阶段实施"
          description: "先 MVP 再迭代完善"
```

### Task
用于启动架构评审子代理。

```yaml
tool: Task
parameters:
  subagent_type: general-purpose
  prompt: |
    你是一位资深架构师，请评审以下架构设计：
    
    {architecture_description}
    
    请从以下维度进行评估：
    1. 可扩展性
    2. 可靠性
    3. 安全性
    4. 性能
    5. 可维护性
    
    指出潜在风险和改进建议。
```

### Write
用于保存测试计划文档。

```yaml
tool: Write
parameters:
  file_path: "/Users/lihao/.qoderwork/workspace/mnagcxtml4a9p1vc/team-orchestrator/test-plans/test-plan-{name}-{date}.md"
  content: "{完整的 markdown 内容}"
```

---

## 📊 质量检查清单

在输出架构设计前，自我检查：

```yaml
quality_checklist:
  architecture_design:
    - [ ] 数据流图是否清晰？
    - [ ] 技术选型是否合理？
    - [ ] 组件职责是否明确？
    - [ ] 接口定义是否完整？
    
  risk_analysis:
    - [ ] 识别了所有 SPOF 吗？
    - [ ] 有降级方案吗？
    - [ ] 监控告警是否考虑？
    - [ ] 安全威胁是否评估？
    
  test_planning:
    - [ ] 测试金字塔是否合理？
    - [ ] 关键路径是否覆盖？
    - [ ] 性能目标是否明确？
    - [ ] 自动化策略是否可行？
    
  feasibility:
    - [ ] 技术难度是否评估？
    - [ ] 人力资源是否匹配？
    - [ ] 时间估算是否现实？
    - [ ] 依赖风险是否识别？
```

---

## 🚨 安全护栏

### 禁止行为
- ❌ 不跳过范围挑战直接设计
- ❌ 不提供没有故障分析的架构
- ❌ 不忽略安全维度的检查
- ❌ 不提供不可行的测试计划

### 必须警告的情况
- ⚠️ 架构过于复杂 → 建议简化或分阶段
- ⚠️ 引入过多新依赖 → 提醒评估和维护成本
- ⚠️ 单点故障未处理 → 强制要求降级方案
- ⚠️ 测试覆盖率目标过低 → 建议提高到合理水平

---

## 📈 度量指标

### 架构健康度评分

```yaml
architecture_health_score:
  dimensions:
    - simplicity: {weight: 0.20}  # 简单优于复杂
    - scalability: {weight: 0.20}  # 扩展能力
    - reliability: {weight: 0.20}  # 可靠性
    - security: {weight: 0.15}     # 安全性
    - maintainability: {weight: 0.15}  # 可维护性
    - testability: {weight: 0.10}  # 可测试性
    
  thresholds:
    excellent: "≥90 分"
    good: "≥75 分"
    needs_work: "≥60 分"
    critical: "<60 分 → 需要重新设计"
```

### 流转效率

```yaml
flow_metrics:
  average_session_time: "60-120 分钟"
  iterations_before_approval: "2-4 轮"
  conversion_rate_to_build_stage: "≥85%"
  architectural_changes_during_build: "<10%"
```

---

## 🔗 与其他技能的集成

### 上游技能
- **← /office-hours**: 接收设计方案文档
  - 输入：design-doc-{name}.md
  - 提取：功能需求、技术约束、成功标准

### 下游技能
- **→ /design-review**: 传递架构约束和技术要求
  - 输出：architecture-diagrams.md
  - 输出：test-plan.md
  - 输出：failure-mode-analysis.md

### 状态持久化

```yaml
state_storage:
  location: "~/.team-orchestrator/projects/{project_slug}/"
  
  artifacts:
    - architecture_diagrams/: "ASCII 数据流图和测试覆盖图"
    - eng_reviews/: "架构评审记录和决策"
    - test_plans/: "完整的测试计划文档"
    - failure_modes/: "故障模式分析矩阵"
    - parallelization/: "并行开发策略文档"
```

---

## 💡 最佳实践

### 架构设计原则
1. **简单优于复杂**
   - 能用简单方案解决的，不用复杂方案
   - 每增加一层抽象都要有充分理由

2. **约定优于配置**
   - 默认约定减少决策成本
   - 只在必要时提供配置选项

3. **显式优于隐式**
   - 数据流和依赖关系要清晰可见
   - 避免魔法和隐式行为

4. **失败是必然的**
   - 假设所有外部调用都会失败
   - 假设所有输入都可能是恶意的
   - 假设所有资源都会耗尽

### 常见陷阱
1. **过度设计**
   - 为未来可能的需求设计
   - 过早优化性能
   - 过度抽象和通用化

2. **设计不足**
   - 忽略安全性和可靠性
   - 没有考虑扩展性
   - 测试策略不完整

3. **技术驱动而非问题驱动**
   - 因为新技术很酷而使用
   - 而不是因为解决问题需要

---

**版本**: 1.0.0  
**创建日期**: 2026-03-30  
**灵感来源**: [gstack /plan-eng-review](https://github.com/garrytan/gstack)  
**维护者**: emersonli
