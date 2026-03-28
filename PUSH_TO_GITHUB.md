# 推送到 GitHub 指南

技能文件已创建完成！现在需要手动推送到 GitHub。

## 方法一：使用 Git 命令行（推荐）

### 1. 配置 Git 身份（首次使用）

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 2. 设置 GitHub 认证

推荐使用 Personal Access Token (PAT)：

1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token" -> "Generate new token (classic)"
3. 勾选 `repo` 权限
4. 生成并复制 token

### 3. 推送代码

```bash
cd /Users/lihao/.qoderwork/workspace/mnagcxtml4a9p1vc/team-orchestrator

# 如果之前添加了 remote
git remote remove origin

# 使用 token 添加 remote（替换 YOUR_TOKEN 和 YOUR_USERNAME）
git remote add origin https://YOUR_TOKEN@github.com/emersonli/call-agent-team.git

# 推送
git push -u origin main
```

或者使用 SSH（如果你配置了 SSH key）：

```bash
git remote add origin git@github.com:emersonli/call-agent-team.git
git push -u origin main
```

---

## 方法二：使用 GitHub Desktop

1. 下载并安装 [GitHub Desktop](https://desktop.github.com/)
2. 登录 GitHub 账号
3. 选择 "Add Local Repository" -> "Choose..."
4. 选择 `/Users/lihao/.qoderwork/workspace/mnagcxtml4a9p1vc/team-orchestrator` 目录
5. 如果是新仓库，选择 "Publish repository"
6. 填写仓库名称 `call-agent-team`
7. 点击 Publish

---

## 方法三：在 GitHub 网站操作

### 步骤 1: 创建空仓库

1. 访问 https://github.com/new
2. 仓库名：`call-agent-team`
3. 描述：Team Orchestrator Skill for Multi-Agent Framework
4. **不要** 勾选 "Initialize this repository with a README"
5. 点击 "Create repository"

### 步骤 2: 推送现有代码

在终端执行：

```bash
cd /Users/lihao/.qoderwork/workspace/mnagcxtml4a9p1vc/team-orchestrator

# 添加 remote
git remote add origin https://github.com/emersonli/call-agent-team.git

# 推送
git push -u origin main
```

系统会提示输入用户名和密码：
- 用户名：你的 GitHub 用户名
- 密码：使用 Personal Access Token（不是账号密码）

---

## 验证推送成功

推送完成后，访问 https://github.com/emersonli/call-agent-team 应该能看到所有文件：

```
✓ README.md
✓ SKILL.md
✓ configs/teams/dev-team.yaml
✓ configs/roles/product-manager.yaml
✓ configs/roles/frontend-dev.yaml
✓ configs/roles/backend-dev.yaml
✓ configs/roles/qa-engineer.yaml
✓ configs/roles/ui-ux-designer.yaml
✓ configs/roles/devops-engineer.yaml
✓ collaboration/agile-sprint.yaml
✓ collaboration/rapid-response.yaml
✓ examples.md
✓ reference.md
✓ scripts/analyze_task.py
✓ scripts/calculate_team_size.py
```

---

## 后续更新

之后如需更新代码：

```bash
cd /Users/lihao/.qoderwork/workspace/mnagcxtml4a9p1vc/team-orchestrator

# 查看修改
git status

# 添加修改
git add .

# 提交
git commit -m "feat: 添加新功能或修复 xxx"

# 推送
git push
```

---

## 常见问题

### Q: 提示 "Permission denied"

A: 检查：
1. Token 是否有 `repo` 权限
2. 是否是仓库所有者或有写入权限
3. Token 是否过期

### Q: 如何查看当前 remote 配置？

```bash
git remote -v
```

### Q: 如何切换到 SSH 方式？

```bash
git remote set-url origin git@github.com:emersonli/call-agent-team.git
git push -u origin main
```

需要先配置 SSH key：
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
cat ~/.ssh/id_ed25519.pub
# 复制到 https://github.com/settings/keys
```
