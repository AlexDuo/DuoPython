#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 用 generator生成斐波纳挈数列


def fib(max):
    n,a,b = 0,0,1
    while n<max:
        # print(b)
        # yield其实是保存了函数的中断状态，并保存了当前函数的值
        yield b #使用yield记录b将使这个函数变成一个生成器
        a,b = b,a+b
        n = n+1
    return "done"

f=fib(10)

# print(f.__next__())
# print(f.__next__())

# 异常捕获
g = fib(12)
while True:
    try:
        x = next(g)
        print(g)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break
