### 什么是 Supervisord？

Supervisord 是一个用 Python 编写的进程管理工具：

- 启动、停止、重启进程
- 自动重启崩溃的进程
- 管理多个进程（支持组）
- 提供 Web 管理界面（可选）
- 日志收集与轮转

## 配置

### 默认配置文件

| 系统            | 默认配置文件                             |
| ------------- | ---------------------------------- |
| Ubuntu/Debian | `/etc/supervisor/supervisord.conf` |
| CentOS/RHEL   | `/etc/supervisord.conf`            |

```ini
[unix_http_server]
file=/var/run/supervisor.sock   ; UNIX socket 文件，supervisorctl 用它通信
chmod=0700                       ; socket 权限

[inet_http_server]               ; Web 管理界面（可选）
port=127.0.0.1:9001              ; 监听地址和端口
username=user                    ; 登录用户名（可选）
password=pass                    ; 登录密码（可选）

[supervisord]
logfile=/var/log/supervisor/supervisord.log ; 日志文件
pidfile=/var/run/supervisord.pid            ; PID 文件
childlogdir=/var/log/supervisor             ; 子进程日志目录
user=root                                   ; 运行用户

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[supervisorctl]
serverurl=unix:///var/run/supervisor.sock ; 使用 UNIX socket
; serverurl=http://127.0.0.1:9001         ; 或使用 HTTP（如果启用了 inet_http_server）

[include]
files = /etc/supervisor/conf.d/*.conf ; ✅ 重要！推荐把配置放这里
```

### 配置文件

```ini
[program:myapp]
command=python3 /home/ubuntu/myapp/app.py
directory=/home/ubuntu/myapp
user=ubuntu
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/supervisor/myapp.log
stdout_logfile_maxbytes=50MB
stdout_logfile_backups=10
environment=PATH="/usr/bin",PYTHONPATH="/home/ubuntu/myapp"

[program:celery_worker]
command=celery -A backend.celery_app worker --loglevel=info
directory=/pdf2zh
user=root
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/supervisor/celery_worker.log
stdout_logfile_maxbytes=10MB
stdout_logfile_backups=5
priority=200

[program:pdf2zh_app]
command=python pdf2zh.py --flask
directory=/pdf2zh
user=root
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/supervisor/pdf2zh_app.log
stdout_logfile_maxbytes=10MB
stdout_logfile_backups=5
priority=300
```

| 参数                        | 说明                          |
| ------------------------- | --------------------------- |
| `program:myapp`           | 程序名称，唯一标识                   |
| `command`                 | 启动命令                        |
| `directory`               | 工作目录                        |
| `user`                    | 以哪个用户运行（安全建议：不要用 root）      |
| `autostart`               | 是否随系统启动                     |
| `autorestart`             | 崩溃后自动重启                     |
| `redirect_stderr`         | 把 stderr 重定向到 stdout，方便统一日志 |
| `stdout_logfile`          | 日志文件路径                      |
| `stdout_logfile_maxbytes` | 单个日志文件最大大小                  |
| `stdout_logfile_backups`  | 保留几个备份                      |
| `environment`             | 设置环境变量                      |

## 使用

```bash
# Install
apt update && sudo apt install supervisor
# update config
supervisorctl reread
supervisorctl update

# manipulate
supervisorctl start myapp/all
supervisorctl stop myapp/all
supervisorctl restart myapp/all

# get
supervisorctl status
supervisorctl tail myapp
supervisorctl tail myapp stderr

# control
supervisorctl
> status
> start myapp
> stop myapp
> reload
> exit
```

```ba&#39;s
# restart
systemctl restart supervisor
# 开机自启
systemctl enable supervisor
systemctl start supervisor
systemctl status supervisor
```

| 项目            | **Supervisord**                                        | **systemd**                                                                        |
| ------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| 类型            | **进程监控与管理工具**（第三方）                                     | **系统初始化系统 + 服务管理框架**（系统级核心组件）                                                      |
| 开发者           | Supervisor 项目（Python 编写）                               | Lennart Poettering（Red Hat）主导，Linux 社区                                             |
| 是否为系统默认       | ❌ 否，需手动安装                                              | ✅ 是（现代 Linux 发行版默认 init 系统，如 Ubuntu 16.04+、CentOS 7+、Debian 8+）                    |
| 运行权限          | 可在普通用户下运行                                              | 以 PID 1 运行，是系统第一个进程（init）                                                          |
| 设计哲学          | “轻量、专注、简单”                                             | “统一、集成、现代化”                                                                        |
| **进程监控与自动重启** | ✅ 强大，可配置 `autorestart=true`、`startretries`、`exitcodes` | ✅ `Restart=always/on-failure/on-abnormal`，支持 `RestartSec=`、`StartLimitInterval=`   |
| **日志管理**      | ✅ 内置日志重定向到文件，支持轮转，简单直接                                 | ✅ 集成 `journald`，统一收集所有服务日志，支持结构化日志、压缩、查询（`journalctl -u service`）                  |
| **进程组管理**     | ✅ 支持 `[group:x]`，可批量控制多个程序                             | ✅ 通过 `Type=notify`、`KillMode=control-group` 管理进程组，但需每个服务一个 unit 文件                 |
| **依赖管理**      | ❌ 无原生支持（需手动顺序启动）                                       | ✅ 强大依赖：`Wants=`、`Requires=`、`After=`、`Before=`、`BindsTo=` 等                        |
| **启动顺序控制**    | ❌ 手动写脚本控制                                              | ✅ 基于 target（multi-user.target, graphical.target）和依赖树自动排序                           |
| **用户级服务**     | ✅ 支持 `supervisord -c ~/.supervisord.conf`              | ✅ 支持 `systemctl --user`，可管理非 root 用户服务（2015+）                                      |
| **资源限制**      | ❌ 有限（可通过 ulimit 或外部脚本）                                 | ✅ 内置：`MemoryLimit=`、`CPUQuota=`、`IOWeight=`、`TasksMax=` 等 cgroup 控制                |
| **网络与套接字激活**  | ❌ 不支持                                                  | ✅ 支持 `SocketActivation`：服务在有连接时才启动，提升性能与安全性                                        |
| **安全增强**      | ❌ 无                                                    | ✅ `PrivateTmp=`、`ReadOnlyPaths=`、`NoNewPrivileges=`、`CapabilityBoundingSet=` 等安全隔离 |
| **图形化界面**     | ✅ 内置 Web UI（`[inet_http_server]`）                      | ❌ 无内置，但可通过 Cockpit、Webmin 等第三方工具集成                                                 |
| **配置文件格式**    | INI（简单易读）                                              | `.service`、`.socket`、`.target` 等（语法类似 INI，但语义更复杂）                                  |
| **系统集成度**     | 低，独立运行                                                 | 高，整合了 init、rc、cron、logind、udev、tmpwatch、hostnamectl 等多个传统工具                        |
