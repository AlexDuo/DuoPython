#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo


class dog:
    # def __init__是构造函数
    # 构造函数的作用是在实例化的时候做一些类的初始化的工作
    # 在类的构造函数中的变量叫做实例变量，他的作用于是生成的实例中本身
    # 在类中的变量叫做类变量，这个变量所有的实例共有，它的作用于是所有类
    # 当我们使用实例调用一个变量的时候，程序会先寻找实例本身是否有这个变量，如果没有再去类中寻找
    def __init__(self,name):
        self.name = name

    def bulk(self):
        print("%s:is bulking"%self.name)

d1 = dog("Dog 1")

d1.bulk()