Hexo + Acorn<br>
Namesilo Domain + Cloudflare CDN

[简体中文站](https://chs.utclc.top) / [繁体中文站](https://cht.utclc.top)

仓库收到 Push 后自动触发 Github Actions 部署到 Github Pages<br>
同时触发另一个 Action 运行 Python 运行 `traditionalize.py`<br>
使用 OpenCC 与自定义规则批量转换所有文件<br>
然后把转换好后的仓库 git push 覆写到繁中站仓库[UTCLC/website_cht](https://github.com/UTCLC/website_cht)<br>
繁中站仓库收到 Push 后同样自动触发 Action 部署到 Pages<br>
（Action 加了限制，只有当前仓库是 `UTCLC/utclc.github.io` 时才会发送 push 繁中仓库，防止套娃触发）