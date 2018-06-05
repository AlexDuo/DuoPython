#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 把类改写成字典的表现形式
class Foo(object):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        print('__getitem__', key)
        return self.data.get(key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)
        self.data[key] = value

    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()

obj ['name'] = 'Duo Zhang'#自动调用 setitem 方法

# print(obj.data)
#
# print(obj['name']) #自动执行getitem

del obj["name"]



# result = obj['k1']  # 自动触发执行 __getitem__
# obj['k2'] = 'alex'  # 自动触发执行 __setitem__
# del obj['k1']