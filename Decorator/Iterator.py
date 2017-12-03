#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 可以被next() 函数调用并不断返回下一个值得对象称为迭代器 Iterator

# 生成器一定是迭代器 因为生成器都有 __next__()方法
# 而迭代器却不一定是生成器
# list dictionary string 虽然都是可迭代对象，但是他们并不是迭代器，我们可以通过使用iter()函数来将他们转换为迭代器
# 定义a为一个list
a = [1,2,3,4]
# 使用内置函数iter将a变成迭代器 并赋值给b
b=iter(a)
# b.__next__
print(b.__next__())
# 迭代器的计算是惰性的，只有在需要返回下一个数据的时候才会进行计算。
# Iterator甚至可以表示成一个无限大的数据流，例如全体自然数，而List是永远不能存储全体自然数的。