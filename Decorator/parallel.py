#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo
# 我他妈被骗了！！！这不是parallel ！！！！！！！！！！！！shit！！！！！！！！！！！
# 三个线程在运行
# 异步I/O
import time

def consumer(name):
    print('%s 准备吃包子'%name)
    while True:
        baozi = yield   #因为有yield的出现所以它变成了一个生成器

        print('包子[%s]来了，被[%s]吃了'%(baozi,name))


# c=consumer('Duo')
# # next会调用yield但是不会给yield传值
# c.__next__()
# # send既会调用yield也会给yield传值
# c.send('梅菜猪肉')

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("包子铺准备开始蒸包子了！")
    for i in range(10):
        time.sleep(1)
        print("蒸了个包子，分两半")
        # 把两个包子分两半分别传给两个吃包子的人
        c.send(i)
        c2.send(i)



producer("Duo")