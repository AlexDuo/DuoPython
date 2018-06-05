#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# _____________________________________________________
# __doc__
# class A:
#     '''this class is used to print A'''
#     def __init__(self):
#         print("A")
#
#
# print(A.__doc__)  #会输出文本描述文件
# _____________________________________________________


# _____________________________________________________
# from lib.xx improt C 没搞懂
# _____________________________________________________



# _____________________________________________________
# call 方法的使用
class A:
    '''this class is used to print A'''
    def __init__(self,name):
        self.name = name
    def __call__(self, *args, **kwargs):
        print (args,kwargs)
    def __str__(self):
        return "<obj:%s>"%self.name

a1 = A("duozhang")
#
a1(2,3,4,5,name = "Duo Zhang")
# _____________________________________________________


# _____________________________________________________
#  __dict__ 方法 是查看类或对象中的所有成员

print(A.__dict__) #以字典的形式打印出来类的所有属性不包括实例
print(a1.__dict__)#以紫癜性是打印出来所有实例的属性不包括类

# _____________________________________________________

print(a1)