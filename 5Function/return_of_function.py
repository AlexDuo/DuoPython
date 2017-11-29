#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 这证明了return会终止当前函数 Test end不会被运行
def test1():
    print("Test 1 run")
    return 0
    print('Test end')
#
# x接收test1的返回值即0
# Return 可以返回多个值，返回的类型可以有多种包括字符串数字列表字典
x=test1()

print(x)
# x y 称为位置参数，即调用函数传值时 传的内容是位置一一对应的
def test2(x,y):
    print(x)
    print(y)
# 位置参数赋值
test2(1,2)
# 关键字赋值
test2(y=2,x=1)
# 混合赋值的时候 例如 test（3， y=2）这时 3是位置赋值，y=2是关键字赋值 但是这种调用的方法禁止向一个变量多次赋值
# 默认参数就是写形参的时候直接给形参默认赋值了
def test3(v1,v2=3):
    print(v1)
    print(v2)

# 这时我们可以调用test（）如下方法
test3(1)
test3(v1=2,v2=4)
test3(1,v2=3)
