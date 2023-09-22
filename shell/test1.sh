#!/bin/bash
:<<!
echo "Hello, world!"

# 变量和=之间不能有空格
myUrl="https://google.com"
echo ${myUrl}

# 只读变量不能修改，否则报错
#readonly myUrl
myUrl="https://baidu.com"
echo ${myUrl}

# 删除，不能删除只读变量
unset myUrl
echo "-----"
echo ${myUrl}
echo
echo "-----"

for skill in Ada Coffe Action Java; do
	echo "I am good at ${skill}Script"
done
!
# 获取字符串长度
string="abcdefg"
echo ${#string}
echo ${#string[0]}
# -----
# 2023.02.07
echo "Shell传递参数实例："
echo "执行的文件名:$0"
echo "传递的第一个参数：${1}"
echo "传递的第二个参数：$2"
echo "传递的参数个数：  ${#}"
echo "传递的参数以一个字符串显示: ${*}"
echo "传递的参数以多个字符串显示：\"$@\""

echo "-- \$*演示 --"
for i in "$*"; do
    echo $i
done

echo "-- \@演示 --"
for i in "$@"; do
    echo $i
done

# expr是一个表达式计算工具
# 运算符和值之间必须有空格
val=`expr 2 + 2`
echo "2 + 2 = ${val}"

a=10
b=20

val=`expr $a + $b`
echo "a + b : $val"

val=`expr $a - $b`
echo "a - b : $val"

val=`expr $a \* $b`
echo "a * b : $val"

val=`expr $b / $a`
echo "b / a : $val"

val=`expr $b % $a`
echo "b % a : $val"
#条件表达式要放在[]中，并且有空格
if [ $a == $b ]
then
   echo "a 等于 b"
fi
if [ $a != $b ]
then
   echo "a 不等于 b"
fi

# 文件测试运算符
file="~/OneDrive"
if [ -r file ]
then
    echo "文件可读"
else
    echo "文件不可读"
fi

if [ -e file ]
then
    echo "文件存在"
else
    echo "文件不存在"
fi

if [ -L file ]
then
    echo "文件存在并且是个符号链接"
fi
echo ${file}

file="~"
for i in ${file}; do
    echo ${i}
done

num1=100
num2=200
if test $[num1] -ne $num2
then
    echo "两个数不想等"
else
    echo "两个数相等"
fi

if [ ${num1} -eq ${num2} ]
then
    echo "两个数相等"
else
    echo "两个数不相等"
fi

# shell文件调用
source test2.sh
echo "调用的url是：${url}"
