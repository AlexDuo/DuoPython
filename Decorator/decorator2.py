#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo


#
# def foo():
#     print('in the foo')
#     bar()
#
# def bar():
#     print('in the bar')
#
# foo()

# 装饰器使用 高阶函数+内置函数来实现
# 装饰器内置函数使用 *args,**kwargs来实现参数个数与有无参数均可的实现
import time

def deco(func):
    def insi(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print('the execution time of bar is %s'%(end_time-start_time))
    return insi

@deco
def bar():
    time.sleep(1)
    print('in the bar')

def withparamater(name,age):
    print('his name is %s'%name+', and his age is %s'%age)

bar()

withparamater('Duo',27)

