---
name: design-review
version: 1.0.0
description: UI/UX 审计专家 - 80 项视觉和体验审查
domain: software-development
stage: 3-design
input: 前端代码或设计稿
output: UI 审计报告 + 修复建议
nextSkill: qa
previousSkill: plan-eng-review
---

# 🎨 Design Review - UI/UX 审计专家

## 🎯 核心价值

**优秀的設計是看不見的，它讓用戶專注於目標而非界面本身。**

本技能专注于：
- ✅ 80 项全面 UI/UX 审计
- ✅ 自动化问题检测和修复
- ✅ Before/After 对比验证
- ✅ 无障碍和响应式检查

---

## 📋 工作流程

### Step 1: 80 项审计清单

#### 维度 1: 视觉设计 (20 项)

```yaml
visual_design:
  typography:
    - "字体层级是否清晰？(H1 > H2 > H3 > Body)"
    - "字号是否合适？(正文 ≥14px)"
    - "行高是否舒适？(1.4-1.6)"
    - "字体数量是否克制？(≤3 种)"
    
  color:
    - "配色方案是否一致？"
    - "对比度是否符合 WCAG AA？(≥4.5:1)"
    - "主色、辅色、强调色是否明确？"
    - "错误、警告、成功色是否语义化？"
    
  spacing:
    - "间距是否统一？(使用 4/8px 基准)"
    - "对齐是否准确？(左对齐/居中/右对齐)"
    - "留白是否充足？"
    - "内外边距是否一致？"
    
  imagery:
    - "图片质量是否清晰？"
    - "图标风格是否统一？(线性/面性)"
    - "图标尺寸是否一致？"
    - "是否有不必要的装饰元素？"
```

#### 维度 2: 交互设计 (25 项)

```yaml
interaction:
  navigation:
    - "导航是否清晰直观？"
    - "面包屑是否存在？(深层级页面)"
    - "返回按钮是否在预期位置？"
    - "当前选中状态是否明显？"
    
  forms:
    - "表单标签是否清晰？"
    - "必填项是否有标识？"
    - "错误提示是否具体？"
    - "验证是否实时？"
    - "提交后是否有反馈？"
    
  feedback:
    - "加载状态是否显示？"
    - "成功提示是否明确？"
    - "错误处理是否友好？"
    - "空状态是否有引导？"
    
  gestures:
    - "触摸目标是否 ≥44px？"
    - "手势支持是否合理？(滑动、长按)"
    - "双击缩放是否禁用？(非图片区域)"
    - "滚动是否流畅？"
```

#### 维度 3: 响应式设计 (15 项)

```yaml
responsive:
  breakpoints:
    - "移动端 (<768px) 测试通过？"
    - "平板端 (768-1024px) 测试通过？"
    - "桌面端 (>1024px) 测试通过？"
    - "超大屏 (>1440px) 优化？"
    
  mobile:
    - "横向滚动是否避免？"
    - "文字是否需要放大才能读？"
    - "按钮是否易于点击？"
    - "表单输入是否触发正确键盘？"
    
  adaptive:
    - "图片是否自适应？"
    - "表格在小屏幕如何处理？"
    - "导航在移动端是否折叠？"
    - "布局是否灵活？"
```

#### 维度 4: 无障碍 (20 项)

```yaml
accessibility:
  keyboard:
    - "所有功能键盘可访问？"
    - "Tab 顺序是否合理？"
    - "焦点是否可见？"
    - "快捷键是否冲突？"
    
  screen_reader:
    - "图片有 alt 文本？"
    - "表单有关联 label？"
    - "ARIA 标签正确使用？"
    - "跳过导航链接存在？"
    
  focus:
    - "焦点管理是否正确？(模态框)"
    - "焦点陷阱是否实现？"
    - "动态内容焦点移动？"
    
  contrast:
    - "文字对比度 ≥4.5:1?"
    - "大文字对比度 ≥3:1?"
    - "UI 组件对比度 ≥3:1?"
    - "不依赖颜色传达信息？"
```

---

### Step 2: 问题修复循环

```yaml
fix_loop:
  for_each_dimension:
    - run_audit: "执行该维度所有检查项"
    - identify_issues: "记录所有未通过项"
    - classify_severity: |
        Critical: 阻碍使用、违反规范、法律风险
        Major: 严重影响体验、用户困惑
        Minor: 视觉瑕疵、不一致
        
    - auto_fix_if_possible: |
        自动修复:
        - 对比度不足 → 调整颜色
        - 触摸目标<44px → 增加 padding
        - 缺少 alt → 添加描述性文本
        - 表单无验证 → 添加验证规则
        
    - manual_required: |
        需要手动修复:
        - 布局重构
        - 交互逻辑调整
        - 品牌色变更
        - 内容重写
        
    - verify_fix: "截图对比 before/after"
```

---

### Step 3: 生成审计报告

**输出文件**: `design-audit-report-{project-name}-{date}.md`

**报告结构**:

```markdown
# Design Review 审计报告

**项目名称**: {项目名称}  
**审计日期**: {YYYY-MM-DD}  
**审计范围**: {页面/组件列表}  
**总体评分**: {XX}/100

---

## 一、执行摘要

### 评分分布
| 等级 | 数量 | 占比 |
|------|------|------|
| ✅ Pass | 65 | 81% |
| ⚠️ Minor | 10 | 12.5% |
| ❗ Major | 4 | 5% |
| 🚨 Critical | 1 | 1.5% |

### 关键发现
- **Critical**: 登录按钮对比度不足 (2.8:1 < 4.5:1)
- **Major**: 移动端导航菜单遮挡内容
- **改进空间**: 表单错误提示不够具体

---

## 二、详细发现

### 🚨 Critical (必须修复)

#### 问题 #1: 登录按钮对比度不足
- **位置**: `/components/LoginForm.tsx:45`
- **当前值**: 2.8:1
- **要求**: ≥4.5:1 (WCAG AA)
- **影响**: 视障用户无法识别
- **修复**: 
  ```diff
  - background: #666666
  + background: #4A4A4A
  ```
- **状态**: ✅ 已修复

[Before/After 对比图]

---

### ❗ Major (建议修复)

#### 问题 #2: 移动端导航遮挡内容
- **位置**: `/layouts/Header.tsx:78`
- **场景**: iPhone SE 竖屏
- **影响**: 底部 20% 内容被遮挡
- **修复**: 
  ```css
  .mobile-nav {
    max-height: calc(100vh - 60px);
    overflow-y: auto;
  }
  ```
- **状态**: ✅ 已修复

---

### ⚠️ Minor (可选优化)

#### 问题 #3: 图标风格不一致
- **位置**: 首页功能图标
- **问题**: 混用线性和面性图标
- **建议**: 统一为线性图标
- **状态**: ⏳ 待修复

---

## 三、分维度评分

| 维度 | 得分 | 通过率 | 问题数 |
|------|------|--------|--------|
| 视觉设计 | 88/100 | 88% | 3 Minor |
| 交互设计 | 82/100 | 82% | 2 Major, 5 Minor |
| 响应式 | 90/100 | 90% | 2 Minor |
| 无障碍 | 75/100 | 75% | 1 Critical, 2 Major |

---

## 四、修复汇总

### 已修复
- [x] 登录按钮对比度 (Critical)
- [x] 移动端导航遮挡 (Major)
- [x] 表单验证提示 (Major)
- [x] 焦点管理 (Minor)

### 待修复
- [ ] 图标风格统一 (Minor) - 优先级：低
- [ ] 部分间距不一致 (Minor) - 优先级：低

---

## 五、Before/After 对比

### 关键问题修复对比

![登录按钮对比](screenshots/login-button-comparison.png)
*图 1: 登录按钮对比度修复前后对比*

![移动端导航](screenscripts/mobile-nav-comparison.png)
*图 2: 移动端导航修复前后对比*

---

## 六、建议和下一步

### 短期（本周）
- [ ] 修复所有 Critical 问题
- [ ] 修复影响核心流程的 Major 问题

### 中期（本月）
- [ ] 建立设计系统组件库
- [ ] 制定无障碍设计规范
- [ ] 进行用户可用性测试

### 长期（本季度）
- [ ] 定期 Design Review 机制
- [ ] 设计 Token 系统建设
- [ ] 多主题支持

---

**审批**:
- [ ] 设计师确认：__________ 日期：__________
- [ ] 前端负责人确认：__________ 日期：__________
```

---

## 🔧 工具调用规范

### AskUserQuestion
用于确定审计范围和重点。

```yaml
tool: AskUserQuestion
parameters:
  questions:
    - question: "这次审计的重点是什么？"
      header: "审计重点"
      multiSelect: true
      options:
        - label: "全面审计"
          description: "80 项完整检查"
        - label: "视觉设计"
          description: "专注视觉层面"
        - label: "交互体验"
          description: "专注交互流程"
        - label: "无障碍"
          description: "专注可访问性"
```

### Bash
用于截图对比和浏览器自动化。

```yaml
tool: Bash
parameters:
  command: |
    # 使用 Playwright 截图
    npx playwright test --screenshot=before
    
    # 应用修复
    npm run fix:ui-issues
    
    # 再次截图对比
    npx playwright test --screenshot=after
```

---

## 📊 质量指标

### 健康度评分计算

```yaml
health_score_calculation:
  formula: |
    Score = (Pass_Count × 1.0) + 
            (Minor_Count × 0.5) + 
            (Major_Count × 0.2) + 
            (Critical_Count × 0)
            
    Final_Score = (Score / 80) × 100
    
  thresholds:
    excellent: "≥90 - 优秀，可直接发布"
    good: "≥75 - 良好，修复 Critical/Major 后发布"
    needs_work: "≥60 - 需要改进"
    critical: "<60 - 需要全面重新设计"
```

---

## 🚨 安全护栏

### 自动修复边界
- ✅ 可以自动修复：颜色对比度、间距大小、alt 文本、aria 标签
- ⚠️ 需要人工确认：布局调整、交互逻辑、品牌色、内容文案
- ❌ 不应自动修改：业务逻辑、数据处理、API 调用

---

**版本**: 1.0.0  
**创建日期**: 2026-03-30  
**灵感来源**: [gstack /design-review](https://github.com/garrytan/gstack)  
**维护者**: emersonli
