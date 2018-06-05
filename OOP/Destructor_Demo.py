#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 析构函数作用：在实例释放或者销毁的时候执行的，通常用于做一些结尾工作，
# 例如关闭一些关闭一些数据库连接和关闭一些打开的临时文件

class humanbeings():
    personality = "active or negative"
    class_list = []

    def __init__(self,name,sex,age,height,weight): #这是一个构造函数
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight

    def __del__(self): #这是一个析构函数
        print("this is a destructor for %s" %self.name)

    def talking(self):
        print("%s is talking" % self.name)


h1 = humanbeings("DUO ZHANG","M","27",'178','75')
# 我们看到析构函数会在对象的所有function执行结束后执行。他会在程序退出或者对象销毁的时候执行
h1.talking()