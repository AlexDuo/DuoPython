#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo
# 在Python中一切皆对象



# class Foo(object):
#     def __init__(self,name):
#         self.name = name
# f = Foo("Duo Zhang")

# 我们称Type 为类的类

# 创建类的第二种方式

# # 定义一个方法
# def func(self):
#     print("hello %s, his age is %s"%(self.name,self.age))
# # 定义一个构造方法
# def __init__(self,name,age):
#     self.name = name
#     self.age = age
#
# # 创建一个类叫FOO type成类 类名FOO 继承（）里面的object可以不写， {以字典的方法加入类的方法 方法名：方法对象}
# Foo = type('Foo',(object,),{'talk':func,'__init__':__init__})
#
# print(type(Foo))
#
# f1 = Foo("Duo zhang",18)
#
# f1.talk()
#

# class MyType(type):
#     def __init__(self,what,base = None, dict = None):


class Foo(object):

    # __metaclass__ = MyType

    def __init__(self,name):
        self.name = name
        print("this is __init__ func for Foo")

    #其实我们通过new来实例化，我们通过new来调用init
    # new是用来创建实例的

    def __new__(cls, *args, **kwargs): # 实例化的时候new 方法会在__init__方法执行
        print("this is the __new__ func for Foo")
        return object.__new__(cls) #去继承父类的new方法


obj = Foo("Duo Zhang")

