#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo
def bulk(self):
    print("%s is bulking"%self.name)

class dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eatting %s"%(self.name,food))


d1 = dog("Tommi")

choice = input("please choose the action of the animal").strip()
# hasattr  has attribute

# print(hasattr(d1,choice))
# print(getattr(d1,choice))
# 通过内存映射出了内存对象地址
if hasattr(d1,choice):
    # func = getattr(d1,choice)
    # func("meat")
    delattr(d1,choice)
    # 删除之后 AttributeError: 'dog' object has no attribute 'name'
else:
    setattr(d1,choice,bulk)
    bulk(d1)


# 反射hasattr 判断一个实例里是否有对应的字符串的方法 hasattr(obj,func_name)
# 反射getattr 根据func_name字符串获取同名的方法的内存地址
print(d1.name)