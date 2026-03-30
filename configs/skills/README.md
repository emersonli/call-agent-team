# 阶段化技能库

本目录包含软件研发领域的深度技能配置，受 [gstack](https://github.com/garrytan/gstack) 启发。

## 🎯 设计理念

传统的团队配置只告诉你"需要多少人"，这些技能提供：
- ✅ **完整的研发流程**：从问题定义到发布上线
- ✅ **阶段化的专业技能**：每个阶段有专门的 AI 技能
- ✅ **自动化测试**：diff-aware 智能测试生成
- ✅ **安全门禁**：发布前的自动化检查
- ✅ **文档自动生成**：设计文档、测试计划、发布说明

## 📋 技能列表

### 1. /office-hours - 问题重构专家

**目的**: 在写代码之前，确保解决的是正确的问题

**触发时机**: 
- 新功能创意
- 产品方向讨论
- 需求模糊不清时

**核心功能**:
- 6 个强制问题深度挖掘需求
- Startup vs Builder 模式选择
- 多方案对比和推荐
- 对抗性评审循环

**输出**: 设计方案文档 + 待解决问题清单

👉 [查看详细技能定义](office-hours/SKILL.md)

---

### 2. /plan-eng-review - 架构设计专家

**目的**: 锁定架构、数据流、技术方案

**触发时机**:
- 开始实施前
- 重大重构前
- 技术方案不明确时

**核心功能**:
- ASCII 数据流图生成
- 测试覆盖图规划
- 架构验证清单（系统设计/依赖/SPOF/安全/运维）
- 故障模式分析
- 测试计划生成
- 并行开发策略

**输出**: 架构图 + 测试计划 + 故障模式分析

👉 [查看详细技能定义](plan-eng-review/SKILL.md)

---

### 3. /design-review - UI/UX 审计专家

**目的**: 80 项视觉和体验审计

**触发时机**:
- 设计稿完成后
- 前端开发完成后
- 上线前的 UI 走查

**核心功能**:
- 4 维度 80 项审计清单
  - 视觉设计（20 项）
  - 交互设计（25 项）
  - 响应式（15 项）
  - 无障碍（20 项）
- 自动修复循环
- Before/After 对比验证

**输出**: UI 审计报告 + 修复建议

👉 [查看详细技能定义](design-review/SKILL.md)

---

### 4. /qa - 智能测试专家

**目的**: Diff-aware 自动化测试生成和执行

**触发时机**:
- 代码提交后
- PR 创建时
- 定期回归测试

**核心功能**:
- Diff-aware 测试生成
  - 基于 git diff 识别影响范围
  - 智能优先级排序
  - 100% 变更代码覆盖
  
- 浏览器自动化
  - $B 工具集成
  - 视觉回归检测
  - Console/Network 监控
  
- 失败分类
  - In-branch failure（新引入）
  - Pre-existing failure（历史遗留）
  - Flaky test（不稳定）
  
- 健康度评分
  - 测试覆盖率（25%）
  - 测试通过率（25%）
  - 代码质量（25%）
  - 性能表现（15%）
  - 安全性（10%）

**输出**: QA 报告 + 健康度评分

👉 [查看详细技能定义](qa/SKILL.md)

---

### 5. /ship - 自动化发布专家

**目的**: 安全、自动化的发布流程

**触发时机**:
- 功能开发完成
- 测试全部通过
- 准备上线

**核心功能**:
- Pre-flight 检查
  - 分支验证
  - Git 状态检查
  - Eng Review 确认
  - QA 报告验证
  
- 并行测试执行
  - Frontend tests
  - Backend tests
  - Integration tests
  - E2E critical tests
  
- 版本号自动升级
  - Semantic versioning
  - Breaking change detection
  - 用户可 override
  
- 发布说明自动生成
  - Conventional commits 解析
  - PR 集成
  - 分组展示（Features/Bug Fixes/Performance...）
  
- 安全门禁
  - 覆盖率门禁（≥60%）
  - Plan audit（TODO 完成情况）
  - Adversarial review（基于 diff size）
  - Verification gate（变更后重测）

**输出**: PR/MR + 发布说明 + 版本标签

👉 [查看详细技能定义](ship/SKILL.md)

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

所有阶段的产物保存在：
```
~/.team-orchestrator/projects/{project_slug}/
├── design_docs/       # 设计方案
├── eng_reviews/       # 架构评审
├── design_audits/     # UI 审计
├── qa_reports/        # QA 报告
└── releases/          # 发布记录
```

---

## 🚀 使用方式

### 完整流程

```bash
# 从创意到发布的完整链路
/office-hours → 生成交互式设计文档
/plan-eng-review → 基于设计文档做架构
/design-review → 完成前端后做 UI 审计
/qa → 提交前自动测试和验证
/ship → 一键生成 PR 和发布说明
```

### 单独使用

```bash
# 仅运行特定技能
/qa              # 仅运行测试和健康检查
/design-review   # 仅做 UI 走查
/ship            # 仅执行发布流程
```

---

## 📊 度量指标

### 健康度评分计算

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
    
    rating = get_rating(total)
    # ≥90: 🟢 Excellent
    # ≥75: 🟡 Good
    # ≥60: 🟠 Needs Work
    # <60: 🔴 Critical
    
    return {'score': round(total, 1), 'rating': rating}
```

---

## 🛡️ 安全护栏

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

### 引导技巧
1. **先问为什么，再问是什么**
   - 先理解动机和目标
   - 再讨论具体功能和方案

2. **用具体数字替代模糊描述**
   - ❌ "很多用户" → ✅ "1000 名月活用户"
   - ❌ "经常使用" → ✅ "每周 3 次，每次 10 分钟"

3. **鼓励用户讲故事**
   - "上一次遇到这个问题是什么时候？"
   - "当时你是怎么解决的？"
   - "如果有一个魔法按钮，你希望它做什么？"

### 常见陷阱
1. **解决方案跳跃**
   - 用户直接说"我要做一个 APP"
   - 应该追问"你想解决什么问题"而非"用什么技术栈"

2. **虚假需求**
   - 用户说"我需要"但没有实际行为支持
   - 需要挖掘真实的使用场景和付费意愿

3. **过度规划**
   - 试图一次性想清楚所有细节
   - 应该聚焦 MVP，快速验证假设

---

## 📚 参考资源

### 推荐阅读
- 《The Lean Startup》- Eric Ries
- 《Zero to One》- Peter Thiel
- 《The Mom Test》- Rob Fitzpatrick
- 《Sprint》- Jake Knapp

### 灵感来源
- [gstack](https://github.com/garrytan/gstack) - Garry Tan 的 AI 结对编程项目
- [ETHOS.md](../../ETHOS.md) - 我们的核心理念
- [ARCHITECTURE.md](../../ARCHITECTURE.md) - 系统架构文档

---

**版本**: 1.0.0  
**创建日期**: 2026-03-30  
**维护者**: emersonli
