#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo
# 引号内部是函数的介绍 函数内容（函数名，注释，函数内容，返回值）
def f1():
    '''testing'''
    print('in the function')
    return 0
# 相比而言一个过程却没有返回值
def p1():
    '''process'''
    print('in the process')

# 调用一个函数,和一个过程
# 他们的区别可以认为是过程就是一个没有返回值的函数
x = f1()
y = p1()

print(x)
print(y)

