# Git快速入门
* [Git简明教程](http://www.runoob.com/manual/git-guide/)
* [Git完整命令手册](http://git-scm.com/docs)
* [PDF版命令手册](github-git-cheat-sheet.pdf)

# Git工作流程
本章节我们将为大家介绍 Git 的工作流程。

一般工作流程如下：

* 克隆 Git 资源作为工作目录。
* 在克隆的资源上添加或修改文件。
* 如果其他人修改了，你可以更新资源。
* 在提交前查看修改。
* 提交修改。
* 在修改完成后，如果发现错误，可以撤回提交并再次修改并提交。
下图展示了 Git 的工作流程：
![git](https://www.runoob.com/wp-content/uploads/2015/02/git-process.png)

# Git 工作区、暂存区和版本库
## 基本概念
我们先来理解下Git 工作区、暂存区和版本库概念

* 工作区：就是你在电脑里能看到的目录。
* 暂存区：英文叫stage, 或index。一般存放在 ".git目录下" 下的index文件（.git/index）中，所以我们把暂存区有时也叫作索引（index）。
* 版本库：工作区有一个隐藏目录.git，这个不算工作区，而是Git的版本库。
下面这个图展示了工作区、版本库中的暂存区和版本库之间的关系：
![git](http://www.runoob.com/wp-content/uploads/2015/02/1352126739_7909.jpg)
# Git 创建仓库
## git init
Git 使用 git init 命令来初始化一个 Git 仓库，Git 的很多命令都需要在 Git 的仓库中运行，所以 git init 是使用 Git 的第一个命令。
在执行完成 git init 命令后，Git 仓库会生成一个.git目录，该目录包含了资源的所有元数据，其他的项目目录保持不变（不像 SVN 会在每个子目录生成 .svn 目录，Git 只在仓库的根目录生成 .git 目录）。
`$ git init`

