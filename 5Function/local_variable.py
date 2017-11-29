#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# local variable 局部变量
# 如下例子中说明 After 所在的value就是一个局部变量，Before所在的变量是全局变量
# 局部变量的作用于制作用于该函数中
value = 'Before'
def modifyvalue(value):
    print('before changing',value)
    value='After'
    print('After changing',value)


modifyvalue(value)

print(value)

#当我们想在函数中修改全局变量的时候,我们可以使用如下的方法
testvalue1 = 'this is the global variable1'
testvalue = 'this is the global variable'
def test(testvalue1):
    global testvalue
    testvalue = 'now this is the global variable'
    print(testvalue)

test(testvalue)

print(testvalue)