# 协作模式库

协作模式按领域分类组织，请根据任务领域选择相应的协作模式。

## 📂 目录结构

```
collaboration/
├── README.md                      # 本文件 - 协作模式索引
├── software/                      # 软件研发领域
│   ├── agile-sprint.yaml         # 敏捷冲刺模式
│   └── rapid-response.yaml       # 快速响应模式
└── government/                    # 政府行政领域
    └── three-provinces-six-ministries.yaml  # 三省六部制工作流程 (待创建)
```

## 🖥️ 软件研发领域

### Agile Sprint (敏捷冲刺)

**适用场景**:
- 功能迭代开发
- 产品 MVP 构建
- 快速试错项目
- 需求变化频繁

**核心特点**:
- 2 周一个 Sprint
- 完整的 Scrum 仪式
- 持续集成和交付

**配置文件**: [software/agile-sprint.yaml](software/agile-sprint.yaml)

### Rapid Response (快速响应)

**适用场景**:
- 紧急项目（<2 周交付）
- MVP 快速验证
- 黑客松项目
- 危机公关需求

**核心特点**:
- 日循环开发
- 最小化流程
- 每晚可演示

**配置文件**: [software/rapid-response.yaml](software/rapid-response.yaml)

## 🏛️ 政府行政领域

### 三省六部制工作流程

**适用场景**:
- 政策制定
- 行政管理
- 公共事务
- 法规出台

**核心特点**:
- 决策、审议、执行三分离
- 相互制衡
- 逐级汇报

**配置文件**: [government/three-provinces-six-ministries.yaml](government/three-provinces-six-ministries.yaml) (待创建)

## 🔄 跨领域通用模式

以下模式适用于多个领域（规划中）:

- **Waterfall (瀑布流)**: 需求明确的大型项目
- **Kanban (看板)**: 运维、支持等持续性工作
- **Matrix (矩阵式)**: 多项目并行的组织

## 使用指南

### 在团队配置中引用

```yaml
# 示例：dev-team.yaml
scenarios:
  - scenarioId: mvp-development
    collaborationModes:
      - modeRef: ../collaboration/software/agile-sprint.yaml
        phase: development
        weight: 0.8
```

### AI 自动选择

AI 会根据以下因素自动推荐协作模式：

1. **任务紧急程度**
   - 紧急 → Rapid Response
   - 常规 → Agile Sprint

2. **项目规模**
   - 小型 (<2 周) → Rapid Response
   - 中型 (2-8 周) → Agile Sprint
   - 大型 (>8 周) → Agile Sprint + Waterfall

3. **需求确定性**
   - 需求多变 → Agile Sprint
   - 需求稳定 → Waterfall

## 扩展新协作模式

在对应领域目录下创建新的 YAML 文件：

```yaml
modeId: your-mode-id
name: 你的模式名称
category: 领域分类

description: |
  模式描述

applicableScenarios:
  - "适用场景 1"
  - "适用场景 2"

workflow:
  phases:
    - phase: phase-1
      name: 阶段 1
      # ...
```

---

**维护者**: emersonli  
**最后更新**: 2026-03-28
