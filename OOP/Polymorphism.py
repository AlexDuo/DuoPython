#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 多态 即 一种接口多重实现 多态就是为了实现接口的重复使用
# Python 没有语法直接支持多态，但是可以间接实现

class Animal:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def animal_talk(obj):
         obj.talk()

class dog(Animal):
    def __init__(self,type):
        super(dog, self).__init__(type)

    def talk(self):
        print("WOOF!")

class cat(Animal):
    def __init__(self,type,barging):
        super(cat, self).__init__(type)

    def talk(self):
        print("MEOW!")



dog1 = dog("dahuang")


Animal.animal_talk(dog1)

