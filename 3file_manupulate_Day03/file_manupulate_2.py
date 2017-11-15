#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

f = open("Victory",'r',encoding='utf-8')

# for i in range(5):
#     print(f.readline())
# 根据输出我们可以知道readlines里面是列表。

# for index,line in enumerate(f.readlines()):
#     if index == 9:
#         print("-----我是第9行的分隔符-----")
#         continue
#     print(line.strip())


# 全部加载后循环
# for line in f.readlines():
#     print(line.strip())

# 一行一行的读（内存中每次只进栈一行）
# count = 0
# for line in f:
#     if count == 9:
#         print("--------我是分隔符-------")
#         count += 1
#         continue
#     print(line.strip())
#     count +=1

# tell 是自述指针所在的位置， read（X）X指代的是读多少个字符，读后指针在所读的最后一个字符上。
print(f.read(10))
print(f.tell())
# 回到某一个角标位置
f.seek(0)
print(f.readline())
# 打印文件编码
print(f.encoding)
# python 读取文件是调用操作系统的I/O接口进行读取
print(f.fileno())
# 打印文件名字
print(f.name)
# 并不是所有的设备都可以SEEK 所以有的seekable
print(f.seekable())
# 判断文件是否可读
# 判断文件是否可写
f.read()
f.writable()
# 强制刷新
# 比如我们已写的方式打开一个文件，我们写入一个新条目，如果某些原因断电或者终止操作，我们写入的内容或许还在缓存中
# 写入一个东西并不是直接写入到硬盘因为直接写入硬盘会很慢，所以写入会首先存入缓存中，而且并不是每次写入一条进入缓存后然后再
# 将这条写入硬盘，我们会规定一个缓存区域，当缓存区域满了之后会写入硬盘。所以强制刷新会在buffer没有满的情况下，将缓存区中
# 的内容直接写入硬盘
print(f.flush())

# 截段
# f.truncate(5)

