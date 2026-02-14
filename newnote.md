.net.md

**.NET 与 .NET Framework 的关系** 是 .NET 开发者必须厘清的核心概念。很多人混淆这两者，其实它们是**不同代际、不同架构、不同目标的平台**。

---

## ✅ 一句话总结：

> **.NET Framework 是微软在 2002–2019 年推出的“传统 Windows 专属 .NET 平台”**  
> **.NET（.NET 5/6/7/8/9）是微软在 2020 年起推出的“统一、跨平台、现代化”的下一代 .NET 平台**
> 
> 👉 **.NET Framework 是“过去”，.NET（5+）是“现在和未来”**  
> 👉 **.NET 5+ 不是 .NET Framework 的升级版，而是它的“继任者”和“替代品”**

---

## 📊 对比表：.NET Framework vs .NET（5+）

| 对比项 | .NET Framework | .NET（5、6、7、8、9） |
| --- | --- | --- |
| **发布时间** | 2002 年（1.0） | 2020 年（.NET 5） |
| **平台支持** | ❌ 仅 Windows | ✅ Windows / macOS / Linux |
| **跨平台** | ❌ 不支持 | ✅ 完全支持 |
| **架构目标** | 专为 Windows 桌面/服务器设计 | 统一所有平台（桌面、Web、云、移动、IoT） |
| **版本命名** | .NET Framework 1.0 ~ 4.8 | .NET 5 → .NET 6 → .NET 7 → .NET 8 → .NET 9 |
| **是否开源** | ❌ 部分开源（后期） | ✅ 完全开源（GitHub） |
| **性能** | 较慢，依赖 GDI+、Win32 | 更快，现代化 JIT（RyuJIT）、AOT、GC 优化 |
| **部署方式** | 依赖系统安装（GAC） | 自包含部署（Self-contained）、单文件发布 |
| **支持的 UI 框架** | WinForms、WPF | WinForms、WPF、MAUI（跨平台桌面/移动） |
| **是否仍在更新** | ❌ 2024 年起停止支持（仅安全更新至 2029） | ✅ .NET 8（LTS）支持到 2026 年，.NET 9 支持到 2027 年 |
| **推荐使用** | ❌ 仅维护遗留系统 | ✅ **所有新项目必须使用 .NET 8/9** |

---

## 🧩 关系图解：它们是如何演进的？

```
.NET Framework 1.0 (2002)
     ↓
.NET Framework 2.0 (2005)
     ↓
.NET Framework 3.5 (2007) —— 加入 LINQ、WCF、WF
     ↓
.NET Framework 4.0 (2010)
     ↓
.NET Framework 4.8 (2019) —— 最后一个版本，停止功能更新
     ↓
     🚫 2020 年微软宣布：不再开发 .NET Framework 新功能！
     ↓
.NET 5 (2020) —— 统一 .NET Framework + .NET Core + Xamarin + Mono
     ↓
.NET 6 (2021) —— 第一个 LTS（长期支持）版本
     ↓
.NET 7 (2022)
     ↓
.NET 8 (2023) —— 当前 LTS，推荐用于生产
     ↓
.NET 9 (2024) —— 最新版本，推荐尝鲜
```

> 💡 **.NET 5 是一个里程碑**：它把原来分散的 .NET 平台（Framework、Core、Xamarin、Mono）**统一成一个平台**，命名为 `.NET`，去掉了“Core”二字。

---

## ❓ 常见误解澄清

### ❌ 误解 1：“我用的是 .NET Framework，它还能用吗？”

> ✅ **能用，但不推荐新项目！**  
> .NET Framework 4.8 仍可运行，微软会提供**安全更新至 2029 年**（仅限 Windows 10/11/Server），  
> 但**不再添加新功能、不支持跨平台、性能落后**。

---

## ✅ 你应该用哪个？

| 你的场景 | 推荐选择 |
| --- | --- |
| ✅ 新建一个桌面应用（WinForms/WPF） | 👉 **.NET 8 或 .NET 9** |
| ✅ 新建一个 Web API / 微服务 | 👉 **.NET 8 或 .NET 9** |
| ✅ 维护一个 10 年前的老系统 | 👉 继续用 .NET Framework 4.8（但尽快计划迁移） |
| ✅ 开发跨平台应用（Mac/Linux） | 👉 **.NET 8/9 + MAUI** |
| ✅ 想用最新功能（如 Source Generators、AOT、性能优化） | 👉 **.NET 9** |
| ✅ 企业生产环境，求稳定 | 👉 **.NET 8（LTS）** |

> ✅ **.NET 8 是当前最推荐的版本**（LTS，支持到 2026 年）

---

## 🚀 迁移建议：从 .NET Framework 到 .NET 8/9

如果你正在维护 .NET Framework 项目，想升级：

| 步骤  | 建议  |
| --- | --- |
| 1   | 评估依赖：是否使用了 **仅限 .NET Framework 的库**（如 `System.Web`、`Entity Framework 6`） |
| 2   | 替换：EF6 → **Entity Framework Core**；WCF → **gRPC / REST API** |
| 3   | 重构：将 WebForms → **ASP.NET Core MVC / Blazor** |
| 4   | 测试：在 .NET 8 上运行并验证功能 |
| 5   | 部署：支持 Windows 10/11，性能更好，体积更小 |

> ✅ 微软提供官方迁移指南：  
> 🔗 https://learn.microsoft.com/zh-cn/dotnet/core/porting/

---

## 总结：.NET 可实现的项目类型一览表

| 类型  | 适用框架 | 跨平台？ | 推荐场景 |
| --- | --- | --- | --- |
| Web API | ASP.NET Core | ✅ 是 | 后端服务、微服务 |
| Web 应用 | ASP.NET Core MVC / Razor Pages | ✅ 是 | 企业网站、后台系统 |
| 前端 Web | Blazor (Server/WASM) | ✅ 是 | 用 C# 开发前端 |
| 桌面（Windows） | WinForms / WPF | ❌ 否 | 传统 Windows 应用 |
| 桌面/移动跨平台 | .NET MAUI | ✅ 是 | 新项目首选 |
| 移动应用 | .NET MAUI | ✅ 是 | iOS/Android App |
| 云函数 | Azure Functions | ✅ 是 | 事件驱动、无服务器 |
| 容器化 | Docker + ASP.NET Core | ✅ 是 | 云原生部署 |
| RPC 服务 | gRPC | ✅ 是 | 高性能微服务通信 |
| 命令行工具 | Console App | ✅ 是 | 工具、脚本、自动化 |
| 游戏  | Unity / MonoGame | ✅ 是 | 2D/3D 游戏开发 |
| AI/ML | ML.NET | ✅ 是 | 本地预测、数据分析 |
| IoT | .NET for IoT | ✅ 是 | 树莓派、传感器 |
| 库   | Class Library | ✅ 是 | 代码复用、NuGet 包 |




docker

| 网络模式 | 参数  | 说明  |
| --- | --- | --- |
| host模式 | -–net=host | 容器和宿主机共享 Network namespace。 |
| container模式 | –-net={id} | 容器和另外一个容器共享 Network namespace。 kubernetes 中的pod就是多个容器共享一个 Network namespace。 |
| none模式 | –-net=none | 容器有独立的Network namespace，但并没有对其进行任何网络设置，如分配 veth pair 和网桥连接，配置IP等。 |
| bridge模式 | -–net=bridge | 默认为该模式 ，通过 -p 指定端口映射。 |

- bridge模式
  ​ docker run -itd -p 8080:80 nginx:latest

> bridge 模式 是默认模式，即使是 使用 `docker run -itd nginx:latest` 命令启动容器，也会创建一个虚拟 IP。

![img](https://k8s.whuanle.cn/1.basic/images/docker_bridge.png)

- none模式

这种网络模式下容器只有 lo 回环网络，没有其他网卡，这种类型的网络没有办法联网，外界也无法访问它，封闭的网络能很好地保证容器的安全性。

创建 none 网络的容器：

```shell
docker run -itd --net=none nginx:latest
```

- host模式

host 模式会让容器与主机共享网络，此时映射的端口可能会生产冲突，但是容器的其余部分(文件系统、进程等)依然是隔离的，此时容器与宿主机共享网络。

- container 模式container 模式可以让多个容器之间相互通讯，即容器之间共享网络。
  
  首先启动一个 A 容器，A 一般为 bridge 网络，接着 B 使用 `–-net={id}` 连接到 A 中，使用 A 的虚拟网卡，此时 A、B 共享网络，可以接着加入 B、C、D 等容器。
  

K8S:

![img](https://k8s.whuanle.cn/1.basic/images/Kubernetes_Architecture_graphic.png)

master 节点中各个组件(控制平面组件)需要使用到的端口：

| 协议  | 方向  | 端口范围 | 作用  | 使用者 |
| --- | --- | --- | --- | --- |
| TCP | 入站  | 6443 | Kubernetes API 服务器 | 所有组件 |
| TCP | 入站  | 2379-2380 | etcd 服务器客户端 API | kube-apiserver, etcd |
| TCP | 入站  | 10250 | Kubelet API | kubelet 自身、控制平面组件 |
| TCP | 入站  | 10251 | kube-scheduler | kube-scheduler 自身 |
| TCP | 入站  | 10252 | kube-controller-manager | kube-controller-manager 自身 |

```bash
# get
docker ps -a
docker pull nginx
docker build -t myapp .

# run and trace
docker run -d --name app -p 8080:80 nginx
docker run -d -p 11010:11010 -v "$(pwd)/amout:/amout" --name auto-update auto-update-app
docker run -d --net=host --name agent pdfai:
docker exec -it app /bin/sh
docker logs -f app
docker -f [--tail 50] logs <容器名或ID>
docker inspect <容器名或ID>
docker update --restart unless-stopped mycontainer

# save
docker save -o nginx.tar nginx:latest
docker load -i nginx.tar

# manipulate
docker stop app
docker rm app
docker kill 55eaa6d88441
docker rmi nginx


# auto restart
docker run -d --name mynginx --restart unless-stopped -p 80:80 nginx
```

docker可以使用.dockerignore语法与.gitignore一致

```.dockerignore
site-packages/
*.tar
test.py
```

dockers compose




git


## Git常用命令

---

### 📊 **初始化与配置**

| 命令  | 说明  |
| --- | --- |
| `git init` | 在当前目录初始化一个新的 Git 仓库 |
| `git clone <url>` | 克隆远程仓库到本地（如：`git clone https://github.com/user/repo.git`） |
| `git config --global user.name "Your Name"` | 设置全局用户名 |
| `git config --global user.email "your.email@example.com"` | 设置全局邮箱 |
| `git config --list` | 查看当前所有 Git 配置信息 |

> ✅ **提示**：首次使用 Git 时必须配置用户名和邮箱，否则提交会失败。

---

### 📊 **状态与查看**

| 命令  | 说明  |
| --- | --- |
| `git status` | 查看工作区、暂存区和分支状态 |
| `git log` | 查看完整提交历史（作者、时间、信息） |
| `git log --oneline` | 简洁一行显示提交历史 |
| `git log --graph --oneline --all` | 图形化显示分支合并历史 |
| `git diff` | 查看工作区与暂存区的差异 |
| `git diff --cached` 或 `git diff --staged` | 查看暂存区与最新提交的差异 |

> 📌 常用组合：`git status` → `git diff` → `git add` → `git commit`

---

### 📥 **添加与提交**

| 命令  | 说明  |
| --- | --- |
| `git add <文件名>` | 将指定文件加入暂存区 |
| `git add .` | 添加当前目录下所有修改和新增文件 |
| `git add -u` | 只添加已跟踪文件的修改（不包括新文件） |
| `git commit -m "提交信息"` | 提交暂存区内容到本地仓库 |
| `git commit -a -m "提交信息"` | 跳过 `add`，直接提交所有已跟踪文件的修改 |

> ⚠️ `git commit -a` 不会添加新文件（untracked files），仅处理已跟踪文件。

---

### 🌿 **分支管理**

| 命令  | 说明  |
| --- | --- |
| `git branch` | 列出所有本地分支 |
| `git branch -a` | 列出所有本地和远程分支 |
| `git branch <分支名>` | 创建新分支（不切换） |
| `git checkout <分支名>` | 切换分支（传统方式） |
| `git switch <分支名>` | 切换分支（Git 2.23+ 推荐） |
| `git checkout -b <分支名>` | 创建并切换到新分支 |
| `git switch -c <分支名>` | 创建并切换到新分支（Git 2.23+） |
| `git merge <分支名>` | 将指定分支合并到当前分支 |
| `git branch -d <分支名>` | 删除已合并的分支 |
| `git branch -D <分支名>` | 强制删除分支（即使未合并） |

> 💡 推荐使用 `git switch` 替代 `git checkout`，语义更明确。

---

### 🌐 **远程仓库操作**

| 命令  | 说明  |
| --- | --- |
| `git remote -v` | 查看远程仓库地址（fetch/push） |
| `git remote add origin <url>` | 添加远程仓库（通常命名为 origin） |
| `git push origin <分支名>` | 推送本地分支到远程 |
| `git push origin <分支名> --set-upstream` | 首次推送并设置上游跟踪分支 |
| `git push` | 推送当前分支到其上游分支 |
| `git pull` | 拉取远程分支并自动合并（= git fetch + git merge） |
| `git fetch` | 仅下载远程更新，不自动合并 |
| `git remote remove origin` | 删除远程仓库关联 |

> 🔁 推荐流程：`git pull` → 开发 → `git add` → `git commit` → `git push`

---

### 🚫 **撤销与回退**

| 命令  | 说明  |
| --- | --- |
| `git restore <文件>` | 丢弃工作区修改（恢复到上次提交状态） |
| `git restore --staged <文件>` | 从暂存区取消添加（保留工作区修改） |
| `git reset HEAD <文件>` | 取消暂存（等价于 `restore --staged`） |
| `git reset --hard HEAD` | 彻底丢弃所有本地修改，回退到最新提交 |
| `git reset --soft HEAD~1` | 回退一次提交，保留修改到暂存区 |
| `git reset --mixed HEAD~1` | 回退一次提交，保留修改到工作区（默认） |
| `git revert <commit-hash>` | 创建一个新提交来撤销指定提交（**安全推荐**） |

> ✅ 团队协作中优先使用 `git revert`，避免破坏历史；个人开发可用 `reset`。

---

### 🧊 **暂存与恢复（Stash）**

| 命令  | 说明  |
| --- | --- |
| `git stash` | 暂存当前所有未提交的修改（工作区 + 暂存区） |
| `git stash list` | 查看所有暂存记录 |
| `git stash apply` | 恢复最近一次暂存内容（不删除记录） |
| `git stash pop` | 恢复并删除最近一次暂存 |
| `git stash drop` | 删除最近一次暂存 |
| `git stash clear` | 清空所有暂存记录 |
| `git stash push -m "备注"` | 带备注暂存（便于识别） |

> 💡 适用场景：临时切换分支，但当前修改未完成时。

---

### 🧹 **其他实用命令**

| 命令  | 说明  |
| --- | --- |
| `git clean -n` | 预览将被删除的未跟踪文件（安全测试） |
| `git clean -f` | 删除未跟踪文件 |
| `git clean -fd` | 删除未跟踪文件和空目录 |
| `git tag` | 列出所有标签 |
| `git tag <name>` | 创建轻量标签（如 `v1.0`） |
| `git tag -a v1.0 -m "发布版本1.0"` | 创建带注释标签 |
| `git push origin --tags` | 推送所有标签到远程仓库 |
| `git show <tag>` | 查看标签对应提交的详细信息 |

> 🏷️ 标签常用于发布版本（Release），如 `v2.1.3`。

---

### ✅ **使用建议汇总**

| 类型  | 推荐做法 |
| --- | --- |
| **新用户** | 先配置 `user.name` 和 `user.email` |
| **日常开发** | `git status` → `git diff` → `git add` → `git commit` → `git push` |
| **分支管理** | 使用 `git switch` 和 `git restore`（现代 Git） |
| **团队协作** | 优先用 `git revert` 撤销他人提交，避免 `reset --hard` |
| **清理工作区** | 用 `git clean -n` 先预览，再 `git clean -fd` 删除 |
| **版本发布** | 使用带注释标签 `git tag -a` + `git push --tags` |















go


- [GO项目架构](#go项目架构)
- [基础语法](#基础语法)
  - [iota](#iota)
  - [control struct](#control-struct)
    - [if](#if)
    - [switch](#switch)
    - [for](#for)
  - [Fun](#fun)
    - [变长参数](#变长参数)
    - [defer](#defer)
    - [make](#make)
    - [new](#new)
  - [Collection and Struct](#collection-and-struct)
    - [容器赋值](#容器赋值)
    - [结构体](#结构体)
  - [interface](#interface)

---

## GO项目架构

### Envirment

```bash
$GOROOT 表示 Go 在你的电脑上的安装位置
$GOBIN 表示编译器和链接器的安装位置，默认是 $GOROOT/bin， Go 1.0.3 及以后的版本置空后将会使用默认值
$GOPATH 默认采用和 $GOROOT 一样的值，但从 Go 1.1 版本开始，你必须修改为其它路径。它可以包含多个 Go 语言源码文件、包文件和可执行文件的路径，而这些路径下又必须分别包含三个规定的目录：src、pkg 和 bin，这三个目录分别用于存放源码文件、包文件和可执行文件。
```

因为垃圾回收和自动内存分配的原因，Go 语言不适合用来开发对实时性要求很高的软件。

Go 1.0.3 版本开始，不再使用 8g，8l 之类的指令进行程序的构建，取而代之的是统一的 `go build` 和 `go install`

- `go build` 编译自身包和依赖包
  
- `go install` 编译并安装自身包和依赖包
  
  **`go install` 默认将可执行文件安装到 `GOPATH/bin` 目录下**，  
  如果你没有设置 `GOPATH`，默认是 `$HOME/go/bin`（即 `~/go/bin`
  
- `go run .`
  
- `go fix` 用于将你的 Go 代码从旧的发行版迁移到最新的发行版
  
- `go test` 是一个轻量级的单元测试框架
  
- `go mod tidy` 自动下载 `import` 中用到的第三方包。
  

| `Bash` | 详情  |
| --- | --- |
| `go mod init 模块名` | 创建 `go.mod` 文件 |
| `go mod tidy` | 下载依赖，同步 `go.mod` 和 `go.sum` |
| `go mod download` | 手动下载依赖（一般不需要） |
| `go mod verify` | 验证依赖是否被篡改 |
| `go list -m all` | 查看所有依赖树 |
| `go get 包名@版本` | 升级/降级依赖版本 |

`go.mod` 是 **Go 模块的配置文件**，用来定义：

- 你的项目模块名（即导入路径）
- Go 的版本
- 项目依赖的第三方包及其版本

`go.sum` 是 **依赖模块的校验和文件**，记录了每个依赖模块的每个版本的加密哈希值。

- 确保你下载的依赖没有被篡改（安全校验）
- 实现可复现构建（reproducible builds）
- 不要手动修改 `go.sum`，Go 工具会自动维护它

## 基础语法

Go 程序的执行（程序启动）顺序如下：

1. 按顺序导入所有被 main 包引用的其它包，然后在每个包中执行如下流程：
2. 如果该包又导入了其它的包，则从第一步开始递归执行，但是每个包只会被导入一次。
3. 然后以相反的顺序在每个包中初始化常量和变量，如果该包含有 init 函数的话，则调用该函数。
4. 在完成这一切之后，main 也执行同样的过程，最后调用 main 函数开始执行程序。

type cast:

```go
valueOfTypeB = typeB(valueOfTypeA)
```

#### iota

`iota` 是 Go 语言中一个**预声明的常量生成器**，它在 `const` 块中使用，用来**自动生成递增的常量值**，非常适合定义枚举（enumerations）。

simple:

```go
const (
    Read   = 1 << iota // 1 << 0 = 1
    Write             // 1 << 1 = 2
    Execute           // 1 << 2 = 4
    Delete            // 1 << 3 = 8
)
```

| `iota` 只在 `const` 中有效 | 在 `var` 或函数中无效 |
| --- | --- |
| 每行递增 | 每个 `const` 行 `iota` +1，不管有没有显式使用 |
| 可被重置 | 新的 `const` 块开始时，`iota` 重置为 0 |
| 支持表达式 | `iota * 2`、`1 << iota`、`iota + 100` 等都合法 |

#### control struct

##### if

```go
if initialization; condition {
    // do something
}
```

##### switch

每一个 `case` 分支都是唯一的，从上至下逐一测试，直到匹配为止。（ Go 语言使用快速的查找算法来测试 switch 条件与 case 分支的匹配情况，直到算法匹配到某个 case 或者进入 default 条件为止。）

一旦成功地匹配到某个分支，在执行完相应代码后就会退出整个 switch 代码块，也就是说您不需要特别使用 `break` 语句来表示结束。

因此，程序也不会自动地去执行下一个分支的代码。如果在执行完每个分支的代码后，还希望继续执行后续分支的代码，可以使用 `fallthrough` 关键字来达到目的。

##### for

无限循环 ：`for { }`

for-range:

```go
for pos, char := range str {
...
}
for key, value := range map1 {
    ...
}
```

#### Fun

##### 变长参数

```go
func myFunc(a, b, arg ...int) {}

myFunc(a, b, slice...) //only slice support slice extend

a := [...]string{"a", "b", "c", "d"}
//[...]string：表示一个 字符串数组，... 是 Go 提供的语法糖，让编译器 自动推断数组长度。
```

##### defer

`defer`允许我们推迟到函数返回之前（或任意位置执行 `return` 语句之后）一刻才执行某个语句或函数（为什么要在返回之后才执行这些语句？因为 `return` 语句同样可以包含一些操作，而不是单纯地返回某个值）。关键字 `defer`的用法类似于面向对象编程语言 Java 和 C# 的 `finally` 语句块，它一般用于释放某些已分配的资源。

当有多个 defer 行为被注册时，它们会以逆序执行(后进先出)

##### make

```go
s := make([]int, 3)      // 长度=3，容量=3
s := make([]int, 3, 5)   // 长度=3，容量=5

m := make(map[string]int)

ch := make(chan int)        // 无缓冲 channel
ch := make(chan int, 10)    // 有缓冲 channel，容量=10
```

about cap:

`len(s) == cap(s)` 时，再 `append` 会触发 **扩容（growing）**

导致：

- 内存分配（`malloc`）
- 数据拷贝（`memcpy`）
- 指针更新

##### new

`new` 是一个**内置函数**，用于**分配内存并返回指向该类型零值的指针**

`new(T)` = **“分配一个 T 类型的零值，并返回它的地址”**

new(int) ⇔ &int{}
new(string) ⇔ &string{}
new(MyStruct) ⇔ &MyStruct{}

#### Collection and Struct

##### 容器赋值

```go
var arrAge := [5]int{18, 20, 15, 22, 16}
var arrLazy := [...]int{5, 6, 7, 8, 22}
var arrList := [5]string{"Chris", "Ron"}
var arrKeyValue := map[int]string{3: "Chris", 4: "Ron"}
```

##### 结构体

```go
type identifier struct {
    field1 type1
    field2 type2
    ...
}

//type 1:
ms := new(struct1)
ms.i1 = 10
ms.f1 = 15.5

//type 2:
ms := &struct1{10, 15.5, "Chris"}

//type 3:
var ms struct1
ms = struct1{10, 15.5, "Chris"}
```

#### interface

接口隐式继承

```go
//define interface
type Speaker interface {
    Speak() string
}

// implement
type Dog struct{}
func (d Dog) Speak() string {
    return "Woof!"
}
type Cat struct{}
func (c Cat) Speak() string {
    return "Meow!"
}

// polymorphism
func MakeSound(s Speaker) {
    fmt.Println(s.Speak())
}

//use
d := Dog{}
c := Cat{}
MakeSound(d) // Woof!
MakeSound(c) // Meow!
```

#### assert

```go
//varI 必须是一个接口变量
if v, ok := varI.(T); ok {  // checked type assertion
    Process(v)
    return
}
```



gradle.md

[https://juejin.cn/post/7234731441074356284]

groovy :

- base

```groovy
def name = "Groovy"  // 动态类型
String greeting = "Hello"  // 显式类型
println "Hello, $name!"  // 字符串插值
def lang = "Groovy"
println "Language: ${lang.toUpperCase()}"  // 插值调用方法
def multiLine = """
    Line 1
    Line 2
"""

def nums = [1, 2, 3]
nums << 4  // 添加元素
println nums[1]  // 访问元素（输出 2）
def map = [key1: "value1", key2: "value2"]
map.key3 = "value3"  // 添加键值对
println map.key1  // 访问值（输出 "value1"）

class Person {   //自动生成 getter/setter
    String name
    Integer age
}
def p = new Person(name: "Alice", age: 30)
println p.name  // 直接访问属性（实际调用 getter）

def square = { num -> num * num }
println square(4)  // 输出 16
// 集合的 each 方法
nums.each { println it }  // it 是隐式参数
```

- DSL
  **Groovy DSL (Domain-Specific Language) 支持**

Groovy 通过 **闭包委托（Closure Delegation）**、**方法拦截** 和 **动态语法** 实现 DSL。
**关键机制**：

- **闭包委托**：将闭包的执行上下文（`delegate`）转移到另一个对象，从而访问其属性和方法。
- **方法缺失（methodMissing）**：动态处理未定义的方法调用。
- **属性缺失（propertyMissing）**：动态处理未定义的属性访问。

```groovy
class ConfigBuilder {
    String serverName
    int port

    void server(Closure closure) {
        closure.delegate = this  // 将闭包委托给当前对象
        closure()               // 执行闭包
    }
}

def config(Closure closure) {
    def builder = new ConfigBuilder()
    closure.delegate = builder
    closure()
}

// 使用 DSL 配置
config {
    server {
        serverName = "myApp"
        port = 8080
    }
}
```

启动配置 ：
/usr/.gradle/ gradle.properties init.gradle settings.gradle

/project/ build.gradle gradle.properties settings.gradle gradlew

1. **/usr/.gradle/init.gradle**: 首先加载全局的初始化脚本。
2. **/project/settings.gradle**: 然后加载项目的 `settings.gradle` 文件，配置项目结构。
3. **/usr/.gradle/gradle.properties**: 接着加载全局的 `gradle.properties` 文件，设置全局属性。
4. **/project/gradle.properties**: 然后加载项目的 `gradle.properties` 文件，设置项目特定的属性。
5. **/project/build.gradle**: 最后加载项目的 `build.gradle` 文件，定义项目的构建逻辑。[https://juejin.cn/post/7234731441074356284]

groovy :

- base

```groovy
def name = "Groovy"  // 动态类型
String greeting = "Hello"  // 显式类型
println "Hello, $name!"  // 字符串插值
def lang = "Groovy"
println "Language: ${lang.toUpperCase()}"  // 插值调用方法
def multiLine = """
    Line 1
    Line 2
"""

def nums = [1, 2, 3]
nums << 4  // 添加元素
println nums[1]  // 访问元素（输出 2）
def map = [key1: "value1", key2: "value2"]
map.key3 = "value3"  // 添加键值对
println map.key1  // 访问值（输出 "value1"）

class Person {   //自动生成 getter/setter
    String name
    Integer age
}
def p = new Person(name: "Alice", age: 30)
println p.name  // 直接访问属性（实际调用 getter）

def square = { num -> num * num }
println square(4)  // 输出 16
// 集合的 each 方法
nums.each { println it }  // it 是隐式参数
```

- DSL
  **Groovy DSL (Domain-Specific Language) 支持**

Groovy 通过 **闭包委托（Closure Delegation）**、**方法拦截** 和 **动态语法** 实现 DSL。
**关键机制**：

- **闭包委托**：将闭包的执行上下文（`delegate`）转移到另一个对象，从而访问其属性和方法。
- **方法缺失（methodMissing）**：动态处理未定义的方法调用。
- **属性缺失（propertyMissing）**：动态处理未定义的属性访问。

```groovy
class ConfigBuilder {
    String serverName
    int port

    void server(Closure closure) {
        closure.delegate = this  // 将闭包委托给当前对象
        closure()               // 执行闭包
    }
}

def config(Closure closure) {
    def builder = new ConfigBuilder()
    closure.delegate = builder
    closure()
}

// 使用 DSL 配置
config {
    server {
        serverName = "myApp"
        port = 8080
    }
}
```

启动配置 ：
/usr/.gradle/ gradle.properties init.gradle settings.gradle

/project/ build.gradle gradle.properties settings.gradle gradlew

1. **/usr/.gradle/init.gradle**: 首先加载全局的初始化脚本。
2. **/project/settings.gradle**: 然后加载项目的 `settings.gradle` 文件，配置项目结构。
3. **/usr/.gradle/gradle.properties**: 接着加载全局的 `gradle.properties` 文件，设置全局属性。
4. **/project/gradle.properties**: 然后加载项目的 `gradle.properties` 文件，设置项目特定的属性。
5. **/project/build.gradle**: 最后加载项目的 `build.gradle` 文件，定义项目的构建逻辑。


k8s.md

```bash
查看 Pod
kubectl get pods -n <ns>
查看日志
kubectl logs -f <pod>
进入容器
kubectl exec -it <pod> -- /bin/sh
描述资源
kubectl describe pod <name>
删除 Pod
kubectl delete pod <name>
更新镜像
kubectl set image deploy/<name> xxx=yyy
回滚
kubectl rollout undo deploy/<name>
查看事件
kubectl get events --sort-by=.metadata.creationTimestamp
查看资源使用
kubectl top pod / node
创建 Secret
kubectl create secret generic xxx
暴露服务
kubectl expose deploy xxx --port=80
```

k9s:

**k9s** 是一个基于终端的、用于管理 **Kubernetes（k8s）** 集群的**交互式可视化工具**



maven.md

maven central repo : https://central.sonatype.com/?smo=true

| scope | 说明  | 示例  |
| --- | --- | --- |
| compile | 编译时需要用到该jar包（默认） | commons-logging |
| test | 编译Test时需要用到该jar包 | junit |
| runtime | 编译时不需要，但运行时需要用到 | mysql |
| provided | 编译时需要用到，但运行时由JDK或某个服务器提供 | servlet-api |

| pram | 说明  |
| --- | --- |
| groupId、artifactId 和 version | 依赖的基本坐标，对于任何一个依赖来说，基本坐标是最重要的，Maven 根据坐标才能找到需要的依赖 |
| type | 依赖的类型，对应于项目坐标定义的 packaging。大部分情况下，该元素不必声明，其默认值是 jar |
| scope | 依赖的范围 |
| optional | 标记依赖是否可选 |
| exclusions | 用来排除传递性依赖 |

- Config mirror:
  ​ ~/.m2/settings.xml

```xml
<settings>
    <mirrors>
        <mirror>
            <id>aliyun</id>
            <name>aliyun</name>
            <mirrorOf>central</mirrorOf>
            <!-- 国内推荐阿里云的Maven镜像 -->
            <url>https://maven.aliyun.com/repository/central</url>
        </mirror>
    </mirrors>
</settings>
```

- CI:

```bash
mvn clean package    
```

- plugins:

```xml
<project>
    ...
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.2.1</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                        <configuration>
                            ...插件配置...
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>

<configuration>
    <transformers>
        <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
            <mainClass>com.itranswarp.learnjava.Main</mainClass>
        </transformer>
    </transformers>
</configuration>
```

- repository:

​ ![1744773046680](file://D:\Note\New\Source\repository.png) 

查找顺序 local repo ->central repo->remote repo

---

````sql
```
mvn clean package

mvn clean package spring-boot:repackage

gradle bootJar # For Spring Boot
gradle jar # Standard Java projects
```
````

| 命令部分 | 作用  |
| --- | --- |
| `clean` | 清理（删除）`target`目录下的所有旧构建文件（如旧的`.class`、`.jar`等），确保每次构建从干净状态开始。 |
| `package` | 执行编译、测试、打包，生成最终的可部署文件（如 JAR/WAR）。 |

### **1. 分步解析**

| 命令部分 | 作用  |
| --- | --- |
| `clean` | 清理（删除）`target`目录下的所有旧构建文件（如旧的`.class`、`.jar`等），确保每次构建从干净状态开始。 |
| `package` | 执行编译、测试、打包，生成最终的可部署文件（如 JAR/WAR）。 |

---

### **2. 完整执行流程**

1. **clean 阶段**
  - 删除项目下的 `target` 目录（如果存在）。
  - 相当于手动执行 `rm -rf target/`。
2. **package 阶段**（包含以下生命周期阶段）
  - **validate** → 检查项目配置是否正确。
  - **compile** → 编译源代码（生成 `.class` 文件到 `target/classes`）。
  - **test** → 运行单元测试（跳过测试可加 `-DskipTests`）。
  - **package** → 打包生成最终文件（如 `your-app-1.0.jar` 或 `.war`）。

---

### **3. 输出结果**

- **普通项目** → `target/your-app-1.0.jar`（标准 JAR，需外部容器运行）。
- **Spring Boot 项目** → `target/your-app-1.0-SNAPSHOT.jar`（可独立运行的 Fat JAR，含嵌入式 Tomcat）。
- **Web 项目** → `target/your-app.war`（需部署到外部 Servlet 容器，如 Tomcat）。

---

### **4. 常见变体命令**

| 命令  | 用途  |
| --- | --- |
| `mvn clean package -DskipTests` | 跳过测试，加速打包（仅编译和打包）。 |
| `mvn clean install` | 打包后，将产物安装到本地 Maven 仓库（`~/.m2/repository/`），供其他项目依赖。 |
| `mvn clean verify` | 执行集成测试（如 Surefire、Failsafe）。 |







