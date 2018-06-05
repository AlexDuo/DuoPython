#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo



class humanbeings():
    personality = "active or negative"
    class_list = []

    def __init__(self,name,sex,age,height,weight):
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight

    def talking(self):
        print("%s is talking" %self.name)


h1 = humanbeings("Duo Zhang","M","27","178","75kg")

h1.talking()

print(h1.sex)
# 这时我们看到当H1实例中没有 personality 这个变量，它会向上查找，找到它所在的类看是否有这个变量
print(h1.personality)
# 我们看到humanbeings类中并没有 eyecolor这个属性，但是我们强制在实例化后的实例中给这个属性赋值，也是可以执行的
h1.eyecolor = "BLK"

print(h1.eyecolor)

h1.personality ="non"
print(h1.personality)
h1.class_list.append("from h1")
h2 = humanbeings("Duo Zhang","M","27","178","75kg")
h2.class_list.append("from h2")
print(h2.personality)

print(h2.class_list)
# 类变量的用途是描述同一类型实例公用的属性，节省资源
