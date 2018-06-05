#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo
# 属性方法

class dog:

    def __init__(self,name):
        self.name = name
        self.__food = None


    @property #把一个方法变成一个静态属性
    def eat(self):
        print("%s is eating %s" %(self.name,self.__food))

    @eat.setter #setter方法要在 属性方法之后
    def eat(self,food):
        print("set the food as: %s" %food)
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print("food has been deleted")

d1 = dog("Tommi")
# 属性不能传参数，但是属性可以赋值，变为类方法的方法也不能直接赋值(需要通过方法名.setter设置)
d1.eat = "Meat"

del d1.eat #设置的deleter方法后，可以通过调用 del.eat 将属性方法删除

d1.eat



# 普通的属性可以删掉，但是属性方法不可以删掉和更改
# del d1.eat    AttributeError: can't delete attribute 但是我们可以通过setter方法进行删除