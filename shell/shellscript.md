### shell教程
Shell 是一个用 C 语言编写的程序，它是用户使用 Linux 的桥梁。Shell 既是一种命令语言，又是一种程序设计语言。

`#!` 告诉系统其后路径所指定的程序即是解释此脚本文件的 Shell 程序。

运行shell脚本的两种方法：
1. 作为可执行程序运行：cd到脚本路径下，赋予可执行权限，**一定写成./xxx.sh执行**，如果写成xxx.sh系统会到PATH里寻找该文件，但是当前目录通常不在PATH里。
```shell
./xxx.sh
```
2. 作为解释器参数执行eg：
```shell
/bin/bash xxx.sh
```

#### shell变量
##### 定义变量
定义变量时，变量名不加美元($)符号，**变量名和等号之间不能有空格**：
```shell
x="shell"
```
除了显示的赋值，还可以用语句给变量赋值：
```shell
for file in 'ls /etc'
或
for file in $(ls /etc)
```

##### 使用变量
使用一个定义过的变量，只要在变量名前面加美元符号即可。
```shell
name="zs"
echo $name
echo ${name}
```
变量名外面的花括号是可选的，加不加都行，加花括号是为了帮助解释器识别变量的边界。
```shell
for skill in java c++ python go; do
    echo "I am good at ${skill}Script"
done
```
如果不加花括号，`skillScript`会被当作整体

已被定义的变量，可被重新定义
```shell
skill="c++"
echo ${skill}
skill="python"
echo ${python}
```
##### 只读变量
使用`readonly`命令可将变量定义为只读变量，只读变量的值不能被改变
```shell
myUrl="www.baidu.com"
echo ${myUrl}
readonly myUrl
myUrl="www.google.com" # error
```

##### 删除变量
使用`unset`命令删除变量，变量被删除后不能再次使用，`unset`不能删除只读变量。

##### 变量类型
运行shell时，会同时存在三种变量：
1) 局部变量 局部变量在脚本或命令中定义，仅在当前shell实例中有效，其他shell启动的程序不能访问局部变量。
2) 环境变量 所有的程序，包括shell启动的程序，都能访问环境变量，有些程序需要环境变量来保证其正常运行。必要的时候shell脚本也可以定义环境变量。
3) shell变量 shell变量是由shell程序设置的特殊变量。shell变量中有一部分是环境变量，有一部分是局部变量，这些变量保证了shell的正常运行

##### shell字符串
单引号：
- 单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的；
- 单引号字串中不能出现单独一个的单引号（对单引号使用转义符后也不行），但可成对出现，作为字符串拼接使用。

双引号：
- 双引号里可以有变量
- 双引号里可以出现转义字符

#### shell传递参数
可以在执行脚本时，向脚本传递参数，格式为`$n`，其中`n`代表一个数字，1为执行脚本的第一个参数...`$0`为执行的文件名。

#### shell数组
Shell 数组用括号来表示，元素用"空格"符号分割开。

##### 关联数组
```shell
declare -A array_name
```

#### shell基本运算符
- 算数运算符
- 关系运算符
- 布尔运算符
- 字符串运算符
- 文件测试运算符

expr 是一款表达式计算工具，使用它能完成表达式的求值操作。
eg：
```shell
# 两数相加
val = `expr 2 + 2`
# 表达式被反引号`包围而不是单引号'
# 表达式和运算符之间有空格
```

#### echo命令
用于输出字符串，以及实现复杂的输出格式控制

#### printf命令
和`echo`都是输出命令，但是`printf`可以控制输出的格式。

#### test命令
用于检测某个条件是否成立，可以进行数值、字符和文件三方面的检查。

#### 流程控制
和c语言类似。

#### 函数
定义方式：
```shell
[ function ] funcname[()]
{
    action;
    [return int;]
    # 如果没有return，则以最后一条语句运行结果作为返回值
}
```
函数返回值在调用函数后通过`$?`获取，调用函数使用函数名即可。

#### 重定向
`command > file`：输出重定向到file

`command >> file`：输出以追加的方式重定向到file

`n > file`：文件描述符为n的文件重定向到file

文件描述符0指的是标准输入（STDIN），1（STDOUT），2（STDERR）

#### 文件包含
一个shell文件可以引用另一个文件的内容
```shell
. filename
或
source filename
```