nodejs.md
## 安装 NVM

### Linux/macOS 安装

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
# 或
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
```

安装完成后，重新打开终端或运行：

```bash
#env
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # 加载 nvm
```

## 基本使用

### 安装 Node.js 版本

```bash
nvm install <version>  # 安装指定版本
nvm install node      # 安装最新稳定版
nvm install --lts     # 安装最新的LTS版本
```

### 查看已安装版本

```bash
nvm ls                # 列出所有已安装版本
nvm ls-remote         # 列出所有远程可用版本
```

### 切换 Node.js 版本

```bash
nvm use <version>     # 切换到指定版本
nvm use --lts         # 切换到最新的LTS版本
```

### 设置默认版本

```bash
nvm alias default <version>  # 设置默认版本
```

### 其他常用命令

```bash
nvm current           # 显示当前使用的版本
nvm uninstall <version> # 卸载指定版本
nvm reinstall-packages <version> # 从旧版本重新安装全局npm包到新版本
```

## 注意事项

1. 使用 NVM 安装的 Node.js 版本与系统全局安装的版本是分开的
2. 不同 Node.js 版本间的全局 npm 包不共享
3. 切换版本后，可能需要重新安装全局包
4. Windows 版 NVM 与 Linux/macOS 版在命令上有些差异

## TypeScript 编译

```bash
# 安装 TypeScript 和 @vercel/ncc
npm install -D typescript @vercel/ncc
npx tsc --version




oauth2.md

##

## OAuth 2.0

[OAuth 2.0 的四种方式 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2019/04/oauth-grant-types.html) 

> OAuth 引入了一个授权层，用来分离两种不同的角色：客户端和资源所有者。......资源所有者同意以后，资源服务器可以向客户端颁发令牌。客户端通过令牌，去请求数据。

**OAuth 2.0 规定了四种获得令牌的流程**:

- 授权码（authorization-code）
- 隐藏式（implicit）
- 密码式（password）：
- 客户端凭证（client credentials）

![OAuth2Type](file://D:\Note\New\Source\OAuth2_Type.png)

```url
https://b.com/oauth/authorize?
  response_type=code&
  client_id=CLIENT_ID&
  redirect_uri=CALLBACK_URL&
  scope=read
```

```url
https://a.com/callback#
 token=ACCESS_TOKEN
```

```url
https://b.com/oauth/token?
 client_id=CLIENT_ID&
 client_secret=CLIENT_SECRET&
 grant_type=authorization_code&
 code=AUTHORIZATION_CODE&
 redirect_uri=CALLBACK_URL
```

```url
{    
  "access_token":"ACCESS_TOKEN",
  "token_type":"bearer",
  "expires_in":2592000,
  "refresh_token":"REFRESH_TOKEN",
  "scope":"read",
  "uid":100101,
  "info":{...}
}
```

## 更新令牌

令牌的有效期到了，如果让用户重新走一遍上面的流程，再申请一个新的令牌，很可能体验不好，而且也没有必要。OAuth 2.0 允许用户自动更新令牌。

具体方法是，B 网站颁发令牌的时候，一次性颁发两个令牌，一个用于获取数据，另一个用于获取新的令牌（refresh token 字段）。令牌到期前，用户使用 refresh token 发一个请求，去更新令牌。

> ```javascript
> https://b.com/oauth/token?
>   grant_type=refresh_token&
>   client_id=CLIENT_ID&
>   client_secret=CLIENT_SECRET&
>   refresh_token=REFRESH_TOKEN
> ```

上面 URL 中，`grant_type`参数为`refresh_token`表示要求更新令牌，`client_id`参数和`client_secret`参数用于确认身份，`refresh_token`参数就是用于更新令牌的令牌。

B 网站验证通过以后，就会颁发新的令牌。

## appendix（keycloak）

对于Keycloak的所有操作都要经过认证，包括访问REST接口，没有携带有效token的话会报401未授权。获取Token主要有两种方式，一是账号+密码，二是clientid+secret。

```shell
password:
curl --location --request POST 'keycloak-dev.cloudrnd.cn:9000/auth/realms/Rewards/protocol/openid-connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=Rewards_admin_local ' \
--data-urlencode 'username=yx.wan' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'password=123456'
```

```shell
secret:
curl --location --request POST 'keycloak-dev.cloudrnd.cn:9000/auth/realms/Rewards/protocol/openid-connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=Rewards_admin_local ' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'client_secret=03d96bec-6bf9-44ae-b492-0d709d28208e'
```

# Log

---

# WebClient

---

# Datasouce

---

#



pdf.md

## 一、PDF 文件结构（PDF Structure）

PDF 并非简单的“图片+文字”混合体，而是一个**层次化、模块化的二进制或文本格式文件**，由多个对象组成。了解基本结构有助于理解为什么有些操作困难（如排版错乱）。

### 1. **PDF 的四大核心组成部分**

| 组成部分 | 功能说明 |
| --- | --- |
| **对象（Objects）** | PDF 中的一切内容都由“对象”表示，如文本、图像、字体、页面等。常见类型：<br> - 数字、字符串<br> - 字典（描述属性）<br> - 数组（存储多个值）<br> - 流（存储图像、压缩数据） |
| **交叉引用表（xref）** | 记录每个对象在文件中的字节偏移位置，便于快速查找和更新。 |
| **文件尾部（Trailer）** | 包含指向“根对象（Catalog）”和“xref表”的指针，是打开PDF的“入口”。 |
| **目录（Catalog）** | 相当于PDF的“大脑”，定义文档结构：<br> - 页面树（Pages）<br> - 编码信息<br> - 元数据（Metadata）<br> - 安全权限等 |

### 2. **页面结构（Page Tree）**

- 页面不是线性排列的，而是通过**树状结构**组织。
- 每个页面是一个独立对象，包含：
  - 内容流（Content Streams）：绘制文字、图形的指令
  - 资源字典（Resources）：引用字体、图像、颜色空间等
  - 媒体框（MediaBox）：页面尺寸（如 A4 = [0 0 595.276 841.89]）

> ✅ 举例：当你删除第3页时，软件会修改页面树，重新链接前后页面。

### 3. **线性化（Web优化）与增量更新**

- **线性化PDF**：为网页快速加载设计，允许边下载边阅读。
- **增量更新**：某些编辑工具不重写整个文件，而是“追加”修改内容。这可能导致文件变大或隐藏旧数据（隐私风险）。

---

## 二、PDF 内容流指令列表(Stream)

### **1. 图形状态管理（Graphics State）**

| 指令  | 含义  | 示例  | 效果  |
| --- | --- | --- | --- |
| `q` | 保存当前图形状态 | `q` | 保存当前颜色、线宽、变换等 |
| `Q` | 恢复上一个保存的状态 | `Q` | 恢复到 `q` 之前的状态 |
| `cm` | 变换矩阵（平移/缩放/旋转） | `1 0 0 1 100 200 cm` | 将坐标原点移到 (100, 200) |
| `w` | 设置线宽 | `2 w` | 线宽变为 2pt |
| `J` | 设置线端点样式 | `1 J` | 圆头端点 |
| `j` | 设置线连接样式 | `1 j` | 圆角连接 |
| `M` | 设置斜接限值 | `10 M` | 斜接最大长度为 10 倍线宽 |
| `d` | 设置虚线模式 | `[5 3] 0 d` | 画 5pt，空 3pt，从 0 开始 |
| `GS` | 应用图形状态字典 | `/GS1 GS` | 应用透明度（需在资源中定义） |

### **2. 颜色设置（Color）**

| 指令  | 含义  | 示例  | 效果  |
| --- | --- | --- | --- |
| `RG` | 设置描边 RGB 颜色 | `1 0 0 RG` | 描边为红色 |
| `rg` | 设置填充 RGB 颜色 | `0 1 0 rg` | 填充为绿色 |
| `K` | 设置描边 CMYK 颜色 | `0 0.5 0.5 0 K` | 描边为青绿 |
| `k` | 设置填充 CMYK 颜色 | `0 0 0 1 k` | 填充为黑色 |
| `G` | 设置描边灰度 | `0.5 G` | 描边为中灰 |
| `g` | 设置填充灰度 | `0.8 g` | 填充为浅灰 |
| `SCN` | 设置任意颜色空间描边 | `0.2 0.4 0.6 SCN` | 用当前颜色空间设色 |

### **3. 路径操作（Path Construction）**

| 指令  | 含义  | 示例  | 效果  |
| --- | --- | --- | --- |
| `m` | 移动到点 | `100 200 m` | 移动到 (100,200) |
| `l` | 画直线到点 | `150 250 l` | 从当前点画线到 (150,250) |
| `c` | 画三次贝塞尔曲线 | `100 200 150 250 200 200 c` | 控制点控制曲线 |
| `v` | 画从当前点开始的曲线（第一个控制点重合） | `150 250 200 200 v` |     |
| `y` | 画到当前点结束的曲线（第二个控制点重合） | `100 200 150 250 y` |     |
| `h` | 闭合路径 | `h` | 从当前点画线回起点 |
| `re` | 画矩形 | `50 500 100 80 re` | 等价于 `m l l l h` |

### **4. 描边与填充（Path Painting）**

| 指令  | 含义  | 示例  | 效果  |
| --- | --- | --- | --- |
| `S` | 描边路径 | `S` | 用当前描边颜色画线 |
| `s` | 描边并关闭路径 | `s` | 等价于 `h S` |
| `f` | 填充路径（非零环绕） | `f` | 用当前填充颜色填充 |
| `F` | 同 `f`（旧版） | `F` |     |
| `f*` | 填充路径（奇偶环绕） | `f*` | 奇偶规则填充（用于镂空） |
| `B` | 填充 + 描边 | `B` | `f S` 的快捷 |
| `B*` | 奇偶填充 + 描边 | `B*` |     |
| `b` | 填充 + 描边 + 关闭 | `b` | `f* S` 的快捷 |
| `b*` | 奇偶填充 + 描边 + 关闭 | `b*` |     |
| `n` | 结束路径（不描边/填充） | `n` | 用于定义剪切路径 |

### **5. 文本操作（Text）**

| 指令  | 含义  | 示例  | 效果  |
| --- | --- | --- | --- |
| `BT` | 开始文本块 | `BT` | 开始文本绘制 |
| `ET` | 结束文本块 | `ET` | 结束文本绘制 |
| `Tm` | 设置文本矩阵（位置+旋转） | `1 0 0 1 100 500 Tm` | 文本位置 (100,500) |
| `Td` | 相对移动文本位置 | `10 -20 Td` | 向右10，向下20 |
| `TD` | 相对移动 + 行间距 | `10 -20 TD` | 同 Td，但设置行高 |
| `T*` | 换行  | `T*` | 等价于 `Td 0 -leading` |
| `Tf` | 设置字体和大小 | `/F1 12 Tf` | 使用字体 F1，12pt |
| `Tj` | 显示字符串 | `(Hello World) Tj` | 显示文本 |
| `TJ` | 显示字符串（带字符间距） | `[ (Hello) -5 (World) ] TJ` | “Hello” 和 “World” 之间空 5pt |
| `'` | 换行并显示字符串 | `(Line 1) '` | 等价于 `(Line 1) T*` |
| `"` | 换行 + 设置字距/词距 | `2 1 (Text) "` | 字距2，词距1 |

### **6. 图像（Image）**

| 指令  | 含义  | 示例  | 效果  |
| --- | --- | --- | --- |
| `BI` | 开始图像数据（内联图像） | `BI ... EI` | 嵌入图像数据（不推荐，用 XObject） |
| `ID` | 图像数据开始 | `ID` | 在 `BI` 和 `EI` 之间 |
| `EI` | 图像数据结束 | `EI` |     |
| `Do` | 显示 XObject 图像 | `/Im0 Do` | 显示名为 `/Im0` 的图像 |

### **7. 剪切路径（Clipping）**

| 指令  | 含义  | 示例  | 效果  |
| --- | --- | --- | --- |
| `W` | 设置裁剪路径 | `50 500 100 80 re W` | 后续绘图只在矩形内可见 |
| `n` | 结束路径（不绘图） | `n` | 用于 `W` 后清空路径 |

### **8. 其他重要指令**

| 指令  | 含义  | 示例  | 效果  |
| --- | --- | --- | --- |
| `sh` | 使用阴影图案填充 | `/Sh1 sh` | 需定义渐变或图案 |
| `MP` | 标记点（用于可访问性） | `MP /Artifact` | 标记装饰性元素 |
| `DP` | 定义标记属性 | `DP /BDC ... EMC` | 用于结构化内容（PDF/UA） |
| `BDC` | 开始标记内容 | `BDC` |     |
| `EMC` | 结束标记内容 | `EMC` |     |

### 总结：PDF 指令流核心思想

| 类别  | 核心指令 | 用途  |
| --- | --- | --- |
| **状态管理** | `q`, `Q` | 保存/恢复绘图状态 |
| **变换** | `cm` | 平移、缩放、旋转 |
| **颜色** | `RG`, `rg`, `K`, `k` | 设置描边/填充颜色 |
| **路径** | `m`, `l`, `c`, `re`, `h` | 构造形状 |
| **绘制** | `S`, `f`, `B` | 描边、填充、组合 |
| **文本** | `BT`, `ET`, `Tf`, `Tj`, `TJ` | 绘制文字 |
| **图像** | `/Im0 Do` | 插入图片 |
| **裁剪** | `W`, `n` | 限制绘图区域 |

```pdf
q
2 w           % 线宽 2pt
1 J           % 圆头端点
1 j           % 圆角连接
[5 3] 0 d     % 虚线：5实3空
1 0 0 1 50 500 cm  % 平移到 (50,500)
0 0 m         % 移动到原点
100 100 l     % 画线到 (100,100)
S             % 描边
Q
```

### `cm` 操作符的作用

在PostScript中，`cm` 操作符用于设置当前的变换矩阵（Current Transformation Matrix）。变换矩阵是一个 3x3 的矩阵，但在PostScript中通常表示为 6 个数值，这些数值定义了矩阵的六个元素，具体如下：

其中，`a`、`b`、`c`、`d`、`e` 和 `f` 是由 `cm` 操作符提供的六个数值。

#### 具体数值解析

给定的命令是：

```post
211.493343 0 0 266.858092 -1.084634 -1.060254 cm
```

这表示变换矩阵为：

#### 作用分解

1. **缩放（Scaling）**：
  - `a = 211.493343`：沿 x 轴缩放 211.493343 倍。
  - `d = 266.858092`：沿 y 轴缩放 266.858092 倍。
2. **平移（Translation）**：
  - `e = -1.084634`：沿 x 轴平移 -1.084634 单位。
  - `f = -1.060254`：沿 y 轴平移 -1.060254 单位。
3. **旋转和平移组合**：
  - `b = 0` 和 `c = 0`：表示没有旋转或剪切操作。

#### 具体效果

- **缩放**：图像或文本将沿 x 轴放大 211.493343 倍，沿 y 轴放大 266.858092 倍。
- **平移**：图像或文本将沿 x 轴向左平移 1.084634 单位，沿 y 轴向下平移 1.060254 单位。

---

## 三、PDF 中的字体（Fonts）

字体是PDF编辑中最常遇到的问题之一。很多“文字乱码”或“无法编辑”的根源在于字体处理不当。

### 1. **字体嵌入（Font Embedding）**

PDF 可以将使用到的字体**部分或全部嵌入**文件中：

| 类型  | 说明  | 是否可编辑 |
| --- | --- | --- |
| **完全嵌入** | 整个字体打包进PDF | 安全，跨设备一致 |
| **子集嵌入** | 只包含文档中用到的字符（如“你好世界”只嵌入这4个字） | 常见于小文件，但无法输入新字 |
| **未嵌入** | 依赖用户系统字体 | 显示可能错乱，编辑困难 |

> 🔍 检查方法：用 Adobe Acrobat 打开 → **文件 → 属性 → 字体**，查看是否“已嵌入”。

### 2. **常见字体问题**

| 问题  | 原因  | 解决方案 |
| --- | --- | --- |
| 文字显示为方块或乱码 | 字体未嵌入，且本地无该字体 | 安装对应字体 或 重新生成PDF |
| 修改文字后字体变化 | 替换字体失败 | 使用编辑工具指定新字体 |
| 无法输入中文 | 缺少中文字体支持 | 使用支持CJK的PDF工具（如WPS、Acrobat） |

### 3. **推荐做法**

- 编辑时尽量使用**系统自带字体**（如黑体、宋体、Arial、Helvetica）。
- 导出PDF时选择“**嵌入所有字体**”或“子集嵌入”。
- 避免使用特殊艺术字体，除非确定对方也能看到。





python.md
## 库文件

### pip 使用

```sh
# config
pip config list
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# information
pip list
pip show requests(packages name)
python -c "import site; print(site.getsitepackages())"
#sys.path 是一个列表，包含了 Python 解释器在导入模块时会搜索的路径。当你有多个路径需要查找时，Python 会按照 sys.path 列表中路径的顺序依次进行搜索，直到找到所需的模块或包为止
python -c "import sys; print(sys.path)"

# outline install
pip install --no-index --find-links=./packages -r requirements.txt
# online install
pip install --no-cache-dir -r requirements.txt
```

### pip config的位置

| 配置文件类型 | 路径  |
| --- | --- |
| **用户级配置（推荐）** | `~/.config/pip/pip.conf`（新版）<br>或 `~/.pip/pip.conf`（旧版） |
| **全局配置** | `/etc/pip.conf` |

### pip install的位置

| 系统  | 安装路径 |
| --- | --- |
| **Windows** | `C:\Users\<用户名>\AppData\Roaming\Python\Python3X\site-packages\` |
| **Linux** | `~/.local/lib/python3.X/site-packages/` |

查看所有路径
python -m site

### `.whl` 包下载

离线环境需求

#### pip下载

```sh
pip download requests==2.25.1

pip download requests --no-binary :all:
```

#### PyPI 下载

1. 打开浏览器，访问 [PyPI ](https://pypi.org/)。
2. 在搜索栏中输入你想要下载的包名称（例如 `requests`）。
3. 进入包的详细页面，找到 "Download files" 或 "Files" 部分。
4. 选择你想要的 `.whl` 文件版本并下载。

#### 使用 `conda` 下载

```sh
pip download requests==2.25.1
```

### venv

```sh
#create
python -m venv myvenv
# activate
source ~/myenv/bin/activate
# deactivate
deactivate
```

目录结构

```dir
#linux
venv/
├── bin/           # 可执行程序：python, pip, activate
├── include/       # C 头文件（编译扩展用）
├── lib/           # Python 标准库 + site-packages（核心！）
│   └── python3.10/
│       ├── site-packages/   # pip 安装的包都在这里
│       └── lib-dynload/     # C 扩展模块 (.so)
├── lib64/         # （可选）64位库，常为 lib 的软链接
├── pyvenv.cfg     # 环境配置文件（重要！）
└── share/         # （可选）共享数据（文档、man、i18n）

#windows
venv/
├── Scripts/
│   ├── python.exe
│   ├── pip.exe
│   └── activate.bat
├── Lib/
│   └── site-packages/
├── pyvenv.cfg
└── Include/     # 头文件
```

### pyproject.toml

`pyproject.toml` 是 Python 官方推荐的**现代项目配置文件**，由 [PEP 518 ](https://pep518.pypa.io/)引入，旨在统一 Python 项目的构建、依赖、工具配置。

| 功能  | `requirements.txt` | `pyproject.toml` |
| --- | --- | --- |
| 安装运行时依赖 | ✅ 是 | ✅ 是（`[project.dependencies]`） |
| 安装开发依赖 | ❌ 无标准方式 | ✅ 是（`[project.optional-dependencies]`） |
| 安装构建工具（如 setuptools） | ❌ 手动 | ✅ 是（`[build-system]`） |
| 配置打包（如包名、版本） | ❌ 需 `setup.py` | ✅ 是（`[project]`） |
| 配置测试工具（pytest） | ❌ 需 `pytest.ini` | ✅ 是（`[tool.pytest]`） |
| 配置格式化工具（black、isort） | ❌ 需单独文件 | ✅ 是（`[tool.black]`） |
| 配置类型检查（mypy） | ❌ 需 `mypy.ini` | ✅ 是（`[tool.mypy]`） |
| 项目元信息（作者、描述、许可证） | ❌ 需 `setup.py` | ✅ 是（`[project]`） |

```toml
[project]
name = "pdf2zh"
version = "1.0.1"
description = "Latex PDF Translator"
authors = [{ name = "abc", email = "@gmail.com" }]
license = "AGPL-3.0"
readme = "README.md"
requires-python = ">=3.12,<3.13"
classifiers = [
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
]
dependencies = [
    "requests",
    # for arm64 linux whells
    "pymupdf<1.25.3",
    "peewee>=3.17.8",
    "fontTools",
    "babeldoc>=0.1.22, <0.3.0",
]

[project.optional-dependencies]
backend = [
    "flask",
    "celery",
    "redis"
]
test = [
]
mcp = [
    "mcp>=1.6.0",
]

[dependency-groups]
dev = [
    "black",
    "flake8",
    "pre-commit",
    "pytest",
    "build",
    "bumpver>=2024.1130",
]

[project.scripts]
pdf2zh = "pdf2zh.pdf2zh:main"

[tool.flake8]
ignore = ["E203", "E261", "E501", "W503", "E741"]
max-line-length = 88

[bumpver]
current_version = "1.9.11"
version_pattern = "MAJOR.MINOR.PATCH[.PYTAGNUM]"

[bumpver.file_patterns]
"pyproject.toml" = [
    'current_version = "{version}"',
    'version = "{version}"'
]
"pdf2zh/__init__.py" = [
    '__version__ = "{version}"'
]
```

```bash
## 在项目根目录（包含 pyproject.toml）
# 开发模式 (-e 表示 editable/development mode)
pip install -e .
# 普通模式
pip install .
# 安装可选依赖
pip install "pdf2zh[mcp,test]"       #用户可选
pip install -e ".[dev]"                #开发者可选
```

## UV


register.md

| 根键名称 | 全称  | 作用  | 存储位置（文件路径） |
| --- | --- | --- | --- |
| `HKEY_CLASSES_ROOT` | HKCR | 定义文件扩展名、协议、COM 对象关联等 | **是 HKCU\Software\Classes 和 HKLM\Software\Classes 的合并视图** |
| `HKEY_CURRENT_USER` | HKCU | 当前登录用户的配置信息 | `%USERPROFILE%\NTUSER.DAT` |
| `HKEY_LOCAL_MACHINE` | HKLM | 整台计算机的系统配置（所有用户共享） | `%SystemRoot%\System32\config\*` |
| `HKEY_USERS` | HKU | 所有用户配置文件的根 | 每个用户 `NTUSER.DAT` 的加载实例 |
| `HKEY_CURRENT_CONFIG` | HKCC | 当前硬件配置文件（启动时的硬件设置） | HKLM\SYSTEM\CurrentControlSet\Hardware Profiles\Current |

### `HKEY_CLASSES_ROOT`（HKCR）—— 文件关联与 COM 注册

- **作用**：定义 **文件扩展名**（如 `.txt`, `.exe`）对应的应用程序、**协议**（如 `http://`, `mailto:`）以及 **COM/OLE 对象** 的注册信息。
- **本质**：它**不是独立的存储**，而是 **HKCU\Software\Classes** 和 **HKLM\Software\Classes** 的**合并视图**。
- **优先级**：
  - 如果当前用户在 `HKCU\Software\Classes` 中定义了某个扩展名（如 `.txt` 打开方式），则**优先使用用户设置**。
  - 如果没有，则使用 `HKLM\Software\Classes` 中的系统默认设置。

### `HKEY_CURRENT_USER`（HKCU）—— 当前用户个性化设置

- **作用**：存储**当前登录用户**的个性化配置，只影响当前用户。
- **包含内容**：
  - 桌面背景、主题、屏幕保护程序
  - 软件的用户偏好（如 Notepad++ 的字体、VSCode 的设置）
  - 最近打开的文件列表
  - 环境变量（用户级）
  - 启动项（用户启动程序）
- **存储位置**：`%USERPROFILE%\NTUSER.DAT`
- **特点**：
  - 用户注销后，设置仍保留
  - 新用户登录时，使用默认模板（`NTUSER.DAT` 的副本）
  - 多用户系统中，每个用户有自己的 HKCU

### `HKEY_LOCAL_MACHINE`（HKLM）—— 系统级全局设置

- **作用**：存储**整个计算机**的配置，影响**所有用户**。
- **包含内容**：
  - 已安装的软件（程序列表）
  - 驱动程序、硬件设备信息
  - 系统服务、启动项（系统级）
  - 环境变量（系统级）
  - 安全策略、组策略（部分）
- **存储位置**：
  - `C:\Windows\System32\config\` 下的文件：
    - `SAM`（用户账户和密码）
    - `SECURITY`（安全策略）
    - `SOFTWARE`（软件注册信息）
    - `SYSTEM`（硬件、驱动、启动配置）
    - `DEFAULT`（默认用户配置模板）
- **特点**：
  - 需要管理员权限才能修改
  - 修改错误可能导致系统无法启动
  - 所有用户共享这些设置
 

supervised.md
### 什么是 Supervisord？

Supervisord 是一个用 Python 编写的进程管理工具：

- 启动、停止、重启进程
- 自动重启崩溃的进程
- 管理多个进程（支持组）
- 提供 Web 管理界面（可选）
- 日志收集与轮转

## 配置

### 默认配置文件

| 系统  | 默认配置文件 |
| --- | --- |
| Ubuntu/Debian | `/etc/supervisor/supervisord.conf` |
| CentOS/RHEL | `/etc/supervisord.conf` |

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

| 参数  | 说明  |
| --- | --- |
| `program:myapp` | 程序名称，唯一标识 |
| `command` | 启动命令 |
| `directory` | 工作目录 |
| `user` | 以哪个用户运行（安全建议：不要用 root） |
| `autostart` | 是否随系统启动 |
| `autorestart` | 崩溃后自动重启 |
| `redirect_stderr` | 把 stderr 重定向到 stdout，方便统一日志 |
| `stdout_logfile` | 日志文件路径 |
| `stdout_logfile_maxbytes` | 单个日志文件最大大小 |
| `stdout_logfile_backups` | 保留几个备份 |
| `environment` | 设置环境变量 |

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

```ba's
# restart
systemctl restart supervisor
# 开机自启
systemctl enable supervisor
systemctl start supervisor
systemctl status supervisor
```

| 项目  | **Supervisord** | **systemd** |
| --- | --- | --- |
| 类型  | **进程监控与管理工具**（第三方） | **系统初始化系统 + 服务管理框架**（系统级核心组件） |
| 开发者 | Supervisor 项目（Python 编写） | Lennart Poettering（Red Hat）主导，Linux 社区 |
| 是否为系统默认 | ❌ 否，需手动安装 | ✅ 是（现代 Linux 发行版默认 init 系统，如 Ubuntu 16.04+、CentOS 7+、Debian 8+） |
| 运行权限 | 可在普通用户下运行 | 以 PID 1 运行，是系统第一个进程（init） |
| 设计哲学 | “轻量、专注、简单” | “统一、集成、现代化” |
| **进程监控与自动重启** | ✅ 强大，可配置 `autorestart=true`、`startretries`、`exitcodes` | ✅ `Restart=always/on-failure/on-abnormal`，支持 `RestartSec=`、`StartLimitInterval=` |
| **日志管理** | ✅ 内置日志重定向到文件，支持轮转，简单直接 | ✅ 集成 `journald`，统一收集所有服务日志，支持结构化日志、压缩、查询（`journalctl -u service`） |
| **进程组管理** | ✅ 支持 `[group:x]`，可批量控制多个程序 | ✅ 通过 `Type=notify`、`KillMode=control-group` 管理进程组，但需每个服务一个 unit 文件 |
| **依赖管理** | ❌ 无原生支持（需手动顺序启动） | ✅ 强大依赖：`Wants=`、`Requires=`、`After=`、`Before=`、`BindsTo=` 等 |
| **启动顺序控制** | ❌ 手动写脚本控制 | ✅ 基于 target（multi-user.target, graphical.target）和依赖树自动排序 |
| **用户级服务** | ✅ 支持 `supervisord -c ~/.supervisord.conf` | ✅ 支持 `systemctl --user`，可管理非 root 用户服务（2015+） |
| **资源限制** | ❌ 有限（可通过 ulimit 或外部脚本） | ✅ 内置：`MemoryLimit=`、`CPUQuota=`、`IOWeight=`、`TasksMax=` 等 cgroup 控制 |
| **网络与套接字激活** | ❌ 不支持 | ✅ 支持 `SocketActivation`：服务在有连接时才启动，提升性能与安全性 |
| **安全增强** | ❌ 无 | ✅ `PrivateTmp=`、`ReadOnlyPaths=`、`NoNewPrivileges=`、`CapabilityBoundingSet=` 等安全隔离 |
| **图形化界面** | ✅ 内置 Web UI（`[inet_http_server]`） | ❌ 无内置，但可通过 Cockpit、Webmin 等第三方工具集成 |
| **配置文件格式** | INI（简单易读） | `.service`、`.socket`、`.target` 等（语法类似 INI，但语义更复杂） |
| **系统集成度** | 低，独立运行 | 高，整合了 init、rc、cron、logind、udev、tmpwatch、hostnamectl 等多个传统工具 |



workflow.md

| 概念  | 说明  |
| --- | --- |
| **Workflow（工作流）** | 一个自动化流程，由一个或多个 jobs 组成，由事件触发（如 `push`、`pull_request`）。定义在 `.github/workflows/` 目录下的 YAML 文件中。 |
| **Event（事件）** | 触发工作流的条件，如 `push`、`pull_request`、`schedule`、`workflow_dispatch` 等。 |
| **Job（任务）** | 一组在相同运行器上执行的步骤。一个工作流可以有多个 job，可并行或依赖执行。 |
| **Step（步骤）** | 一个具体的任务，如运行命令、使用 Action、设置环境变量等。 |
| **Action（操作）** | 可复用的单元，封装了常用逻辑（如 `actions/checkout`、`actions/setup-node`）。可以是 GitHub 官方的，也可以是社区的或自定义的。 |
| **Runner（运行器）** | 执行工作流的机器。GitHub 提供 `ubuntu-latest`、`windows-latest`、`macos-latest` 等托管运行器，也支持自托管运行器。 |





npx ncc --version
npm run build
```
