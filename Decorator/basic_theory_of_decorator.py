#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo
import time

# 装饰器本身是函数，功能是用来装饰其他函数的（为其他函数添加附加功能）
# 装饰器原则1：不能修改被装饰的函数的源代码
# 原则2：被装饰函数的调用方式也不能修改

# 装饰器函数
# def timmer(func):
#     def warpper(*args,**kwargs):
#         start_time=time.time()
#         func()
#         stop_time=time.time()
#         print('the func run time is %s' %(stop_time-start_time))
#     return warpper
#
# # 在函数前追加装饰器
# @timmer
# def test1():
#     time.sleep(3)
#     print('in the test 1')
#
#
#
# test1()
# 实现装饰器需要的知识：
# 1.函数即“变量”
# 2.高阶函数
#   a:把一个函数名，当作实参传给另外一个函数（高阶函数的这个特性可以在不修改被装饰函数源代码的情况下为其添加功能）
#   b:返回值中包含函数名（高阶函数的这个特性可以实现不修改函数的调用方式而追加功能）
# 3.嵌套函数 在一个函数内“定义”一个函数
# 4.高阶函数+嵌套函数 -> 装饰器

# 我们首先定义一个ori 原函数，他的功能是睡3秒输出in the ori
def ori():
    time.sleep(3)
    print('in the ori')

# 我们接着定义一个高阶函数，高阶函数的的形参fun 用来以后接收 ori函数，在这个函数中
# print（fun）是追加的功能即为打印传入函数的内存地址，return fun 为返回被传入的函数（保留函数原有功能）
# 当我们调用decori并传入ori的时候我们相当于返回了 ori这个函数并打印了ori函数的内存地址，同时 decori（ori）又是一个函数
# 函数即变量 我们用ori接收这个函数的内存地址，并运行ori 相当于更新了 ori函数的内存地址，没有改变ori的调用方式却改变了函数的功能
def decori(fun):
    print(fun)
    return fun

ori=decori(ori)

ori()
