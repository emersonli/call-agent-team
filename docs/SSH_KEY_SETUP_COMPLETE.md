# SSH Key 配置完成！✅

## 已完成的步骤

1. ✅ 生成了 SSH key
   - 私钥：`~/.ssh/id_ed25519`
   - 公钥：`~/.ssh/id_ed25519.pub`

2. ✅ 公钥已复制到剪贴板

## 📝 接下来需要手动完成的步骤

### 步骤 1: 打开 GitHub SSH Keys 页面

**点击这里直接打开**: https://github.com/settings/keys

或者手动操作：
1. 访问 https://github.com
2. 登录你的账号（emersonli）
3. 点击右上角头像 → Settings
4. 左侧菜单选择 "SSH and GPG keys"

### 步骤 2: 添加 SSH Key

1. 点击 **"New SSH key"** 按钮
2. 填写：
   - **Title**: `QoderWork MacBook`
   - **Key type**: Authentication Key (默认)
   - **Key**: 粘贴下面的内容（已经复制到剪贴板了）：

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILKQQGTNW9AQkEOGraYLKPbjNJuRa2v0OiMp6FZa7PIZ lihao@hao--Macbook.local
```

3. 点击 **"Add SSH key"**
4. 如果提示输入密码，输入你的 GitHub 密码确认

### 步骤 3: 验证连接

添加完成后，在终端执行：

```bash
ssh -T git@github.com
```

如果看到类似以下信息，说明成功：
```
Hi emersonli! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## 🔧 自动推送代码到 GitHub

验证成功后，执行以下命令切换为 SSH 方式并推送：

```bash
cd /Users/lihao/.qoderwork/workspace/mnagcxtml4a9p1vc/team-orchestrator

# 切换 remote 为 SSH
git remote set-url origin git@github.com:emersonli/call-agent-team.git

# 测试推送
git push -u origin main
```

---

## 📋 常用 SSH 命令

### 查看已生成的 key

```bash
ls -la ~/.ssh/
```

### 查看公钥内容

```bash
cat ~/.ssh/id_ed25519.pub
```

### 添加到 ssh-agent（避免每次输入密码）

```bash
# 启动 ssh-agent
eval "$(ssh-agent -s)"

# 添加 key
ssh-add ~/.ssh/id_ed25519
```

### 永久添加到钥匙串（macOS）

```bash
# 编辑或创建 SSH config
cat >> ~/.ssh/config << EOF
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
EOF
```

---

## ❓ 常见问题

### Q: 提示 "Permission denied (publickey)"

A: 说明 SSH key 还没有正确添加到 GitHub。检查：
1. 是否正确复制了整个公钥（包括 `ssh-ed25519` 和后面的内容）
2. 是否在正确的 GitHub 账号下添加
3. 添加后是否刷新了页面确认保存成功

### Q: 可以在多个设备使用同一个 SSH key 吗？

A: 可以！只需要在每个设备上生成 SSH key，然后都添加到 GitHub 即可。GitHub 允许多个 SSH key 关联到同一个账号。

### Q: 如何删除已添加的 SSH key？

A: 在 https://github.com/settings/keys 页面，找到对应的 key，点击 Delete 删除。

### Q: SSH key 会过期吗？

A: 不会！SSH key 没有过期时间，除非你主动删除它。但建议定期轮换（比如每年一次）以提高安全性。

---

## 🎯 下一步

完成上述步骤后，你就可以：

1. ✅ 无需密码推送代码到 GitHub
2. ✅ 在 QoderWork 中安全地使用 Git 功能
3. ✅ 继续开发和更新 team-orchestrator 技能

有任何问题随时告诉我！
