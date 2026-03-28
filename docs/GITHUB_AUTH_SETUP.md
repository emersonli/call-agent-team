# 配置 GitHub 认证（安全方式）

## ⚠️ 重要提示

**不要将 GitHub Token 提交到代码仓库！** GitHub 的 secret scanning 会自动检测并阻止包含 token 的推送。

---

## 方法一：使用 Git Credential Manager（推荐）

### macOS

```bash
# 安装 Homebrew（如果还没有）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装 Git Credential Manager
brew install git-credential-manager
```

然后执行任何 git 操作时，系统会自动弹出浏览器让你登录 GitHub。

### Windows

Git for Windows 自带 Git Credential Manager，首次 push 时会弹出登录窗口。

---

## 方法二：使用 SSH Key（最安全）

### 1. 生成 SSH Key

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

一路回车即可。

### 2. 添加公钥到 GitHub

```bash
cat ~/.ssh/id_ed25519.pub
```

复制输出内容，访问：https://github.com/settings/keys  
点击 "New SSH key"，粘贴公钥，保存。

### 3. 切换 remote 为 SSH

```bash
cd /Users/lihao/.qoderwork/workspace/mnagcxtml4a9p1vc/team-orchestrator
git remote set-url origin git@github.com:emersonli/call-agent-team.git
git push -u origin main
```

---

## 方法三：使用 Personal Access Token（PAT）

### 1. 创建 Token

1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token" -> "Generate new token (classic)"
3. Note: 填写描述（如 "QoderWork Skills"）
4. Expiration: 选择过期时间（建议 90 天）
5. Scopes: 勾选 **`repo`** (Complete control of private repositories)
6. 点击 "Generate token"
7. **立即复制 token**（刷新后就看不到了！）

### 2. 使用 Token

```bash
# 方式 A: 在 URL 中使用（不推荐，会留在历史记录中）
git clone https://YOUR_TOKEN@github.com/emersonli/call-agent-team.git

# 方式 B: 配置 credential helper（推荐）
git config --global credential.helper store

# 然后执行一次 push/pull，输入用户名和 token
git push
# Username: emersonli
# Password: ghp_xxxxxxxxxxxx (粘贴 token)
```

之后 token 会被保存在 `~/.git-credentials`，无需重复输入。

---

## 方法四：使用环境变量（适合脚本）

### 临时设置（当前终端会话有效）

```bash
export GITHUB_TOKEN="ghp_xxxxxxxxxxxx"
git clone https://${GITHUB_TOKEN}@github.com/emersonli/call-agent-team.git
```

### 永久设置（不推荐，有安全风险）

**不要**将 token 明文写入 `~/.zshrc`、`~/.bash_profile` 等文件！

如果一定要用，请使用加密的 secret 管理工具：

#### macOS Keychain

```bash
# 存储 token
security add-generic-password -s github_token -a emersonli -w "ghp_xxxxxxxxxxxx"

# 读取 token（在脚本中使用）
GITHUB_TOKEN=$(security find-generic-password -s github_token -a emersonli -w)
```

---

## 验证配置

```bash
# 测试连接
git remote -v

# 尝试推送
echo "# Test" >> README.md
git add README.md
git commit -m "test"
git push
```

如果成功推送，说明配置正确！

---

## Token 安全管理

### ✅ 最佳实践

- 定期轮换 token（每 90 天）
- 使用最小权限原则（只给需要的 scope）
- 为不同用途创建不同的 token
- 使用 Git Credential Manager 或 SSH key
- 在 CI/CD 中使用 secrets 功能

### ❌ 避免的做法

- 将 token 硬编码在代码中
- 提交包含 token 的文件到 git
- 在日志或错误信息中打印 token
- 通过即时通讯工具发送 token
- 使用永不过期的 token

---

## Token 泄露了怎么办？

1. **立即撤销**: https://github.com/settings/tokens
2. 找到泄露的 token
3. 点击 "Delete"
4. 生成新的 token
5. 更新所有使用该 token 的地方

---

## 常见问题

### Q: 为什么我的 push 被拒绝了？

A: GitHub secret scanning 检测到你的 commit 中包含 token。解决方法：
1. 移除包含 token 的文件
2. 使用 `git reset` 或 `git rebase` 修改历史 commit
3. 重新推送

### Q: 如何查看已保存的 credentials？

```bash
# macOS
cat ~/.git-credentials

# 或者查看 Keychain
security find-generic-password -s github_token
```

### Q: 如何清除保存的 credentials？

```bash
# 删除文件
rm ~/.git-credentials

# 或者清除缓存
git config --global --unset credential.helper
```
