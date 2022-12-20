## linux系统类型

遇到这个问题，源于每次在docker中更新包，不知道何时用yum和apt-get

## 一、linux系统基本上分两大类：

- RedHat系列：Redhat、Centos、Fedora等
- Debian系列：Debian、Ubuntu等 

   如何判断linux的发行版是哪一种呢？可以通过下面的shell脚本判断

```sh
#!/bin/sh
if [ -f /etc/debian_version ]; then
   echo "debian"
elif [ -f /etc/redhat-release ]; then
   echo "centos"
else
   echo "Unknown"
   exit;
fi
```



### 1. RedHat 系列 

- 常见的安装包格式 rpm包,安装rpm包的命令是“rpm -参数” 
-  包管理工具 yum 
-  支持tar包 

### 2. Debian系列

- 常见的安装包格式 deb包,安装deb包的命令是“dpkg -参数”
- 包管理工具 apt-get
- 支持tar包

