#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo
# 打开一个文件要指定这个文件的编码集，因为默认使用系统编码GBK
# data=open("dieyoung",encoding='utf-8').read()
# open("文件名","读或写不写默认是读"，编码读取方式
# w 是创建并写入一个新文件，如果有同名文件则会覆盖
f = open("dieyoung","w",encoding='utf-8')#文件句柄(就是文件的内存对象，包括文件名，字符集，大小，硬盘起始位置)

f.write("this is the new thing")
# data = f.read()
# print(data)

# open 里面可以用"a" append 追加，此时不会重写文件，但是也不可读