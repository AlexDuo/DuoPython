#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 参数组
# 单独使用位置参数赋值，或者关键字赋值的时候，如果定义了函数需要两个参数，那么不能多也不能少
# 当使用默认参数赋值的时候默认参数可以不用赋值。
# 用参数组给函数赋值

def test(*papamters):
    print(papamters)

# 这里都是tuple的形式
test(1,3,4,5,6,7,7,8,98,9)

test(*[2,3,4,5,6,7,8,9])

def test2(x,*par):
    print(x)
    print(par)
#  对于混合赋值的函数，如下的赋值方式是不行的，因为x只会调用位置赋值 其余后面的则是参数组赋值
# test2(1,2,3,4,5,6,7,x=2)
test2(1,2,3,4,5,65)
# 字典的方式
# **kwargs  把n个关键字参数转换成字典
def test3(**kwargs):
    print(kwargs)

test3(name='duo',age=26,sex='M')