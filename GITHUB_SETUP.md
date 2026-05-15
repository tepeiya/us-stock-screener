## GitHub 托管 + 自动更新 操作指南

### 第一步：创建GitHub仓库

1. 打开 https://github.com/new
2. 仓库名填 `us-stock-screener`（或你喜欢的名字）
3. 选 **Public**（公开仓库，免费）
4. 不要勾选任何初始化选项
5. 点击 **Create repository**

### 第二步：推送代码

在 [Open Terminal](minis://open_terminal?init_command=cd%20/var/minis/workspace) 中执行：

```bash
# 配置你的GitHub信息
git config user.email "你的邮箱@example.com"
git config user.name "你的GitHub用户名"

# 添加远程仓库（替换 YOUR_USERNAME 为你的GitHub用户名）
git remote add origin https://github.com/YOUR_USERNAME/us-stock-screener.git

# 推送到GitHub（会弹出登录窗口，输入GitHub token）
git push -u origin master
```

> 推送时需要输入GitHub Personal Access Token（不是密码）
> 创建token: https://github.com/settings/tokens → Generate new token → 勾选 `repo` 权限

### 第三步：启用GitHub Pages（自动部署）

推送成功后：
1. 打开仓库页面 → **Settings** → **Pages**
2. Source 选 **GitHub Actions**
3. 之后每次推送到 `master` 分支，Action会自动部署

### 第四步：配置自动更新

部署完成后的网址格式：
```
https://YOUR_USERNAME.github.io/us-stock-screener/screener.html
```

打开 `version.json` 修改 `version` 字段，用户下次打开就会提示更新。

### 日常更新流程

```bash
cd /var/minis/workspace

# 修改代码后：
git add screener.html screener-data.js  # 只提交改过的文件
git commit -m "feat: 新增XXX功能"
git push
```

**自动触发：** 每次 `git push` → GitHub Actions自动部署 → 用户打开页面自动检测更新并提示刷新

### 关键文件说明

| 文件 | 作用 |
|:----|:-----|
| `version.json` | 版本号+更新日志，修改后用户会收到更新提示 |
| `sw.js` | Service Worker，控制离线缓存和自动更新 |
| `.github/workflows/deploy.yml` | GitHub Actions 自动部署配置 |
| `manifest.json` | PWA配置（添加到桌面时使用） |
