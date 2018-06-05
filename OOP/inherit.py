#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 使用人类做继承的例子
class relation(object):
    def make_friends(self,obj):
        print("%s is making friends with %s"%(self.name,obj.name))
        self.friendlist.append(obj)


class humanbeings:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.friendlist = []

    def eat(self):
        print("%s is eating" %self.name)
    def drink(self):
        print("%s is drinking" %self.name)
    def talk(self):
        print("%s is talking" %self.name)

class man(humanbeings,relation): # man继承了humanbeings
    # 当我们要在父类的基础之上追加新的实例属性
    def __init__(self,name,age,specialorgan):
        # humanbeings.__init__(self,name,age)  继承父类构造函数的第一种方法
        super(man, self).__init__(name,age)   #继承父类构造函数的第二种方法
        self.specialorgan = specialorgan
    def protectfamily(self): #定义了子类的私有方法
        print("%s is a man, he will protect the family")
    def eat(self):
        humanbeings.eat(self)
        print("He eats a lot of food")



m1 = man("Duo Zhang",27,"adam's apple")
m2 = man("Alex","27","adam's apple")

print(m1.name+" born with a special organ named %s" %m1.specialorgan)

m1.make_friends(m2)

print(m1.friendlist[0].name)