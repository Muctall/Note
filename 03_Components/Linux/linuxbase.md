## linux分类

### Redhat

<b>Redhat</b> , 应该称为 Redhat 系列 , 包括 <b>RHEL (Redhat Enterprise Linux</b> , 也就是所谓的 Redhat Advance Server , 收费版本) , <b>Fedora Core</b> (由原来的 Redhat 桌面版本发展而来 , 免费版本) , <b>CentOS</b> (RHEL的社区克隆版本 , 免费) ;

Redhat 应该说是在国内使用人群最多的 Linux 版本 ,  所以这个版本的特点就是使用人群数量大 , 资料非常多 ;

Redhat 系列的包管理方式采用的是基于 `RPM` 包的 `YUM` 包管理方式 , 包分发方式是编译好的二进制文件 ; 稳定性方面 RHEL 和 CentOS 的稳定性非常好 , 适合于服务器使用 , 但是 Fedora Core 的稳定性较差 , 最好只用于桌面应用 ;


### Debian
<b>Debian</b> , 或者称 Debian 系列 , 包括 <b>Debian</b> 和 <b>Ubuntu</b> 等 ; Debian 是社区类 Linux 操作系统的典范 , 是迄今为止最遵循 GNU 规范的 Linux系统 ;

Ubuntu 严格来说不能算一个独立的发行版本 , Ubuntu 是基于 Debian 的 unstable 版本加强而来 , 可以这么说 , Ubuntu 就是一个拥有 Debian 所有的优点 , 以及自己所加强的优点的近乎完美的 Linux 桌面系统 ;

根据选择的桌面系统不同 , 有三个版本可供选择 , 基于 Gnome 的 Ubuntu , 基于 KDE 的 Kubuntu 以及基于 Xfc 的 Xubuntu ; 特点是界面非常友好容易上手 , 对硬件的支持非常全面 , 是最适合做桌面系统的Linux发行版本 ;

Debian 最具特色的是 `apt-get/dpkg` 包管理方式 , 其实 Redhat 的 YUM 也是在模仿 Debian 的 APT 方式 , 但在二进制文件发行方式中 , APT 应该是最好的了 ; Debian 的资料也很丰富 , 有很多支持的社区 , 有问题求教也有地方可去 ;

## 系统

### 目录系统
![](source/linux-directory-structure.webp)
#### FHS（Filesystem Hierarchy Standard）根目录文件


| 目录    | 全称          | 描述                                                                                                                                                                            |
|--------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /bin/  | Binaries     | 存放系统命令，普通用户和 root 都可以执行。放在 /bin 下的命令在单用户模式下也可以执行                                                                                           |
| /boot/ | Boot         | 系统启动目录，保存与系统启动相关的文件，如内核文件和启动引导程序（grub）文件等                                                                                                 |
| /dev/  | Devices      | 设备文件保存位置                                                                                                                                                              |
| /etc/  | Etcetera     | 配置文件保存位置。系统内所有采用默认安装方式（rpm 安装）的服务配置文件全部保存在此目录中，如用户信息、服务的启动脚本、常用服务的配置文件等                                      |
| /home/ | Home         | 普通用户的主目录（也称为家目录）。在创建用户时，每个用户要有一个默认登录和保存自己数据的位置，就是用户的主目录，所有普通用户的主目录是在 /home/ 下建立一个和用户名相同的目录。如用户 liming 的主目录就是 /home/liming |
| /lib/  | Libraries    | 系统调用的函数库保存位置                                                                                                                                                     |
| /media/| Media        | 挂载目录。系统建议用来挂载媒体设备，如软盘和光盘                                                                                                                            |
| /mnt/  | Mount        | 挂载目录。早期 Linux 中只有这一个挂载目录，并没有细分。系统建议这个目录用来挂载额外的设备，如 U 盘、移动硬盘和其他操作系统的分区                                              |
| /misc/ | Miscellaneous| 挂载目录。系统建议用来挂载 NFS 服务的共享目录。虽然系统准备了三个默认挂载目录 /media/、/mnt/、/misc/，但是到底在哪个目录中挂载什么设备可以由管理员自己决定。例如，笔者在接触 Linux 的时候，默认挂载目录只有 /mnt/，所以养成了在 /mnt/ 下建立不同目录挂载不同设备的习惯，如 /mnt/cdrom/ 挂载光盘、/mnt/usb/ 挂载 U 盘，都是可以的 |
| /opt/  | Optional     | 第三方安装的软件保存位置。这个目录是放置和安装其他软件的位置，手工安装的源码包软件都可以安装到这个目录中。不过笔者还是习惯把软件放到 /usr/local/ 目录中，也就是说，/usr/local/ 目录也可以用来安装软件                              |
| /root/ | Root         | root 的主目录。普通用户主目录在 /home/ 下，root 主目录直接在“/”下                                                                                                            |
| /sbin/ | System Binaries | 保存与系统环境设置相关的命令，只有 root 可以使用这些命令进行系统环境设置，但也有些命令可以允许普通用户查看                                                                      |
| /srv/  | Service      | 服务数据目录。一些系统服务启动之后，可以在这个目录中保存所需要的数据                                                                                                          |
| /tmp/  | Temporary    | 临时目录。系统存放临时文件的目录，在该目录下，所有用户都可以访问和写入。建议此目录中不能保存重要数据，最好每次开机都把该目录清空                                        |


#### 非FHS（Filesystem Hierarchy Standard）根目录文件

| 一级目录        | 全称           | 功能（作用）|                                 
|----------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /lost+found/   | Lost and Found | 当系统意外崩溃或意外关机时，产生的一些文件碎片会存放在这里。在系统启动的过程中，fsck 工具会检查这里，并修复已经损坏的文件系统。这个目录只在每个分区中出现，例如，/lost+found 就是根分区的备份恢复目录，/boot/lost+found 就是 /boot 分区的备份恢复目录             |
| /proc/         | Process        | 虚拟文件系统。该目录中的数据并不保存在硬盘上，而是保存到内存中。主要保存系统的内核、进程、外部设备状态和网络状态等。如 /proc/cpuinfo 是保存 CPU 信息的，/proc/devices 是保存设备驱动的列表的，/proc/filesystems 是保存文件系统列表的，/proc/net 是保存网络协议信息的... |
| /sys/          | System         | 虚拟文件系统。和 /proc/ 目录相似，该目录中的数据都保存在内存中，主要保存与内核相关的信息 |

#### Linux /usr目录
usr，全称为 `Unix Software Resource`，此目录用于存储系统软件资源。FHS 建议所有开发者，应把软件产品的数据合理的放置在 /usr 目录下的各子目录中，而不是为他们的产品创建单独的目录。
Linux 系统中，所有系统默认的软件都存储在 /usr 目录下，/usr 目录类似 Windows 系统中 C:\Windows\ + C:\Program files\ 两个目录的综合体。

| 子目录          | 功能（作用）|
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /usr/bin/      | 存放系统命令，普通用户和超级用户都可以执行。这些命令和系统启动无关，在单用户模式下不能执行                                                                                                                |
| /usr/sbin/     | 存放根文件系统不必要的系统管理命令，如多数服务程序，只有 root 可以使用。                                                                                                                                |
| /usr/lib/      | 应用程序调用的函数库保存位置                                                                                                                                                                           |
| /usr/XllR6/    | 图形界面系统保存位置                                                                                                                                                                                  |
| /usr/local/    | 手工安装的软件保存位置。我们一般建议源码包软件安装在这个位置                                                                                                                                          |
| /usr/share/    | 应用程序的资源文件保存位置，如帮助文档、说明文档和字体目录                                                                                                                                            |
| /usr/src/      | 源码包保存位置。我们手工下载的源码包和内核源码包都可以保存到这里。不过笔者更习惯把手工下载的源码包保存到 /usr/local/src/ 目录中，把内核源码保存到 /usr/src/linux/ 目录中                                 |
| /usr/include   | C/C++ 等编程语言头文件的放置目录                                                                                                                                                                      |

#### Linux /var 目录
/var 目录用于存储动态数据，例如缓存、日志文件、软件运行过程中产生的文件等。通常，此目录下建议包含如表 4 所示的这些子目录。
| /var子目录     | 功能（作用）                                                                                                                                                                |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /var/lib/    | 程序运行中需要调用或改变的数据保存位置。如 MySQL 的数据库保存在 /var/lib/mysql/ 目录中                                                                                    |
| /var/log/    | 登陆文件放置的目录，其中所包含比较重要的文件如 /var/log/messages, /var/log/wtmp 等。                                                                                   |
| /var/run/    | 一些服务和程序运行后，它们的 PID（进程 ID）保存位置                                                                                                                       |
| /var/spool/  | 里面主要都是一些临时存放，随时会被用户所调用的数据，例如 /var/spool/mail/ 存放新收到的邮件，/var/spool/cron/ 存放系统定时任务。                                       |
| /var/www/    | RPM 包安装的 Apache 的网页主目录                                                                                                                                         |
| /var/nis 和 /var/yp | NIS 服务机制所使用的目录，nis 主要记录所有网络中每一个 client 的连接信息；yp 是 linux 的 nis 服务的日志文件存放的目录                                              |
| /var/tmp     | 一些应用程序在安装或执行时，需要在重启后使用的某些文件，此目录能将该类文件暂时存放起来，完成后再行删除                                                                      |



### 文件命令
#### 属性
|文件属性与chmod| 
|---|
|-uuugggooo (u,owner)(g,group)(o,other)(a,all)|
|+(加入) -(除去) =(设定)|
|drwxrwxrwx (r,read)(w,write)(x,execute)|
|-421421421|

|命令|全称|参数|语法|备注
|---|---|---|---|---|
|chgrp|change group ownership|`-R,--recursive)`|`chgrp [OPTION]... GROUP FILE...`|-|   
|chown|change owner|`-R`|`chown [OPTION]... [OWNER][:[GROUP]] FILE...`|修改所有者|
|chmod|change mode|`-R`|`chmod [OPTION]... MODE[,MODE]... FILE...`<br>`chmod [OPTION]... OCTAL-MODE FILE...`|修改用户的权限,举例`chmod u=rwx,g=rx,o=r .bashrc`<br>`chmod 777 .bashrc`|


#### 基本处理
|命令|全称|参数|语法|备注|
|---|---|---|---|---|
|ls|list files|`-R`<br>`-a,--all`<br>`-l,--list`<br>`-d,--directory`<br>`-s,--size`:print the allocated size of each file, in blocks<br>`-k,--kibibytes`:default to 1024-byte blocks for disk usage|`ls [OPTION]... [FILE]...`|列出目录及文件名|
|cd|change directory|-|`cd [DIRECTORY]`|切换目录|
|pwd|print work directory|-|`pwd`|显示目前的目录|
|mkdir|make directory|`-m,--mode`:set file mode (as in chmod), not a=rwx - umask<br>`-p,--parents`:no error if existing, make parent directories as needed<br>`-v,--verbose`:print a message for each created directory|`mkdir [OPTION]... DIRECTORY...`|创建一个新的目录|
|rmdir|remove directory|`-p`|`rmdir [OPTION]... DIRECTORY...`|删除一个空的目录|
|cp|copy file|`-R(r)`<br>`-f, --force`<br>`-i, --interactive`:prompt before overwrite<br>`-l,--link`:hard link files<br>`--s, --symbolic-link`:symbolic link files<br>`-d`:same as --no-dereference --preserve=links<br>`-p`:same as --preserve=mode,ownership,timestamps<br>`-a`:same as -pdr<br>`-u,--update`|`cp [OPTION]... SOURCE... DEST`|复制文件或目录|
|rm|remove|`-irf`|`rm [OPTION]... FILE...`|删除文件或目录|
|mv|move|`irf`|`mv [OPTION]... SOURCE... DEST`|移动/重命名文件或目录|

#### 文件内容处理
|命令|全称|参数|语法|备注|
|---|---|---|---|---|
|cat|concatenate and display|`-b, --number-nonblank`: Number nonempty output lines, overrides -n.<br>`-E, --show-ends`: Display $ at the end of each line.<br>`-n, --number`: Number all output lines.<br>`-s, --squeeze-blank`: Suppress repeated empty output lines.<br>`-T, --show-tabs`: Display TAB characters as ^I.<br>`-v, --show-nonprinting`: Use ^ and M- notation, except for LFD and TAB.|`cat [OPTION]... [FILE]...`|由第一行开始显示文件内容|
|tac|concatenate and display in reverse|`-b, --before`:attach the separator before instead of after|`tac [OPTION]... [FILE]...`|从最后一行开始显示，可以看出 tac 是 cat 的倒着写,与cat参数不同|
|nl|number lines of files|`-b, --body-numbering=STYLE`:use STYLE for numbering body lines<br>`-f|`nl [OPTION]... [FILE]...`|显示的时候，顺道输出行号！格式繁杂详见 man|
|more|file perusal filter for crt viewing|`+n`:display next n lines (default is 1)|`more [options] [file]...`|一页一页的显示文件内容，操作指令h or ?   Help: display a summary of  these  commands.   If  you forget all the other commands, remember this one.|
|less|opposite of more|`-N`:line numbers (default off)|`less [options] [file]...`|与 more 类似，但是比 more 更好的是，他可以往前翻页！|
|head|output the first part of files|`-c, --bytes=[-]K`print the first K bytes of each  file;  with  the  leading  '-',print all but the last K bytes of each file<br>`-n, --lines=[-]K` print the first K lines instead of the first 10; with the leading '-', print all but the last K lines of each file|`head [OPTION]... [FILE]...`|只看头几行|
|tail|output the last part of files|`-c, --bytes=K` output the last K bytes; or use -c +K to output  bytes  starting with the Kth of each file<br>`-n, --lines=K` output the last K lines, instead of the last 10; or use -n +K to output starting with the Kth|`tail [OPTION]... [FILE]...`|只看尾几行|


#### 磁盘
|命令|全称|参数|语法|备注|
|---|---|---|---|---|
|df|disk free|`-a,--all`<br>`-h, --human-readable`:print sizes in human readable format (e.g., 1K 234M 2G)<br>`-T,--print-type`print file system type<br>`-i, --inodes`list inode information instead of block usage|`df [OPTION]... [FILE]...`|检查文件系统的磁盘空间占用情况。可以利用该命令来获取硬盘被占用了多少空间，目前还剩下多少空间等信息。|
|du|file space usage|`-ah`|`du [OPTION]... [FILE]...`|对文件和目录磁盘使用的空间的查看|
