#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo
# 静态方法只是名义上归类管理，实际上在静态方法中访问不了类或实例中的任何属性
class dog:
    def __init__(self,name):
        self.name = name

    @staticmethod #静态方法实际上和类没有什么关系 如果将一个类方法前加上@staticmethod意味着将这个方法于类切断了
    # 静态方法名义上是类下的一个类，需要通过类的实例调用
    def eat(self,food):
        print("%s is eating %s" %(self.name,food))



d1 = dog("Tommi")

d1.eat("meat")
