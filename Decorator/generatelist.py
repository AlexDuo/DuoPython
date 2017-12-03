#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 介绍一种新的列表定义方式 （列表生成式）

# list = [ i*2 for i in range(10)]
#
# print(list)


# a = []
# for i in range(10):
#     a.append(i*2)
#
# print(a)
# 列表生成器是边生成边调用
generator = (i*2 for i in range(10))

# for i in generator:
#     print(i)
# 生成器只有在调用的时候才会执行生成过程。（生成相应的数据）
# 当生成器由于某种原因终止在某个点的时候我们可以通过调用  __next()__方法来获取下一个应该生成的数据

print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
# 生成器没有办法回到上一个，生成器只记住当前位置，它及不知道前面是什么也不知道后面是什么，
# 生成器就以这种方式节省内存
