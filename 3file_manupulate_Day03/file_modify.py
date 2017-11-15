#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 实现文件的读写（既能读又能写）r+《读写》读和追加（追加就是放到最后）打开->读->追加
# 《写读》w+ 先创建一个文件 写后再读
# 在源文件上的修改永远是覆盖操作，覆盖对应位置的数值
# rb 是二进制文件读
# wb 是二进制写
f1 = open('Victory','wb')

# f = open("Victory",'r+',encoding= 'utf-8')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.write('------new line after line 3------')
# print(f1.readlines())
# 如果你要写入一个二进制文件，写入的内容必须也是二进制的，例如如下进行转换
f1.write('change this into binary'.encode())