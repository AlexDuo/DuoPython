#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")

class C(A):
    def __init__(self):
        print("C")

class D(B,C):
    pass

new = D()

# 在CLASS D所属的实体中  先找B 然后C 再最后找A 这样的遍历方式叫做广度优先

# py2 经典类是按深度优先继承的，新式类是按广度优先来继承的
# py3 经典类和新式类都是统一按广度优先来继承的