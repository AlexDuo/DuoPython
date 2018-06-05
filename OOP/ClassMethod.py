#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 类方法只能访问类变量，不能访问实例变量
class dog:
    name = "Toby"
    def __init__(self,name):
        self.name = name

    @classmethod
    def eat(self,food):
        print("%s is eating %s" %(self.name,food))



d1 = dog("Tommi")#实例传进去的Tommi并没有被访问

d1.eat("meat")
