#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

import pickle
# 因为当一个方法调用结束他的内存地址会自动清空，所以这里我们需要再生命下这个方法
def greeting(name):
    print("hi %s"%name)

f = open('test2.txt','rb')

# 用loads方法获得 data 这个data就是字典文件了
# data = pickle.loads(f.read())
data = pickle.load(f)
# 调用字典里的func（这是个方法的内存地址）然后传入相应的值
print(data['func']('Duo'))