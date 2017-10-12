#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 字符串一些贼蛋疼的用法，嗯。。。贼蛋疼


name = "duo\tzhang"
print(name.capitalize())#首字母大写

print(name.count("a"))#查找字符串中某个元素的个数

print(name.center(50,"-"))#要打印的变量居中，一共50个字符不够的用-代替

print(name.endswith("ang"))#判断一个字符串是否以相应的字符或字符串结尾，真true假flase

print(name.expandtabs(tabsize=3))#如果你的字符串中间用\t 隔开，这里设定了间隔距离等于多少个空格

print(name.find("o"))#字符在字符串中的位置以0开头

print(name[name.find("z"):0])#字符串切片

# format和format_map 的用法大致相同
lollipop = "this is a {one} {two}"
# 看！这就是他的用法 代表：值，代表：值 以此类推 妈妈再也不用担心我的学习 so easy
print(lollipop.format_map({"one":"delicious","two":"lollipop"}))

print("abcd123".isalnum())#是否是字母表或者数字
# isalpha 是不是纯字母 不区分大小写都行
# isdecimal 是不是十进制
print("ok".isidentifier())#判断该字符是不是标识符(变量名)
# islower 是不是小写
# isnumeric是不是一个数字
# istitle是不是每个单词首字母都大写
# isprintalbe 是不是可以打印的
# issupper是不是全是大写
print("!".join(["日","了","狗"]))#在单个字符链接处join一些东西

print(name.ljust(10,"@"))#总长度不足10在后方用设定的字符补位
print(name.rjust(12,"@"))#总长度不足12在前方用设定的字符补位
# .lower 将字符串中的大写变成小写 .upper变大写
print(name.lstrip())#从左侧去掉字符串的空格或者回车
print(name.rstrip())#从右侧去掉字符串的空格或者回车
print(name.strip())#从两侧去掉字符串的空格或者回车
# 设定了p作为一个翻译器
p = str.maketrans("这是一段密文","123456")
# 字符串.translate()将定义好的翻译器传进去
print("我想对你说这是一段密文".translate(p))

# 替换
print("duo zhang".replace("d","D").replace("z","Z"))

print("aabbccdd".rfind("c"))#找到最右边的c的位置

print("this is a string".split(" ")) #分割字符串到list
print("this.is.a.string".split("."))
print("1\n2\n3".splitlines())
print("Duo Zhang".swapcase())#大小写互换
print("duo zhang".title())#变成一个title
print("用零填充不足".zfill(20))