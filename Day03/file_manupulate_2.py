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