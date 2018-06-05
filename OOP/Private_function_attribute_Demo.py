#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

class humanbeings():
    personality = "active or negative"
    class_list = []

    def __init__(self,name,sex,age,height,weight):
        self.name = name
        self.__sex = sex #在变量追加下划线就会使这个变量变成私有变量(私有属性)
        self.age = age
        self.height = height
        self.weight = weight

    def talking(self):
        print("%s is talking" %self.name)
    def showsex(self): #对外提供方发可以查看，但不可以修改
        print("%s's gender is %s" %(self.name,self.__sex))

h1 = humanbeings("Duo Zhang", "M", "27", "178", "75kg")

# print(h1.__sex)   这时候会报错

h1.showsex()
# 私有方法也是方法名前追加“__”
