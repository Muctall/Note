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
