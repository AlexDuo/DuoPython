#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# Python 中 set的作用可以是去重复，也可以是关系测试
# 集合也是无序的

list_1 = [1,4,6,8,6,7,9]
list_1 = set(list_1) #将List1转换成set，也可以解释成将自己赋值成set
list_2 = set([2,6,66,7,8,9])
# print(list_1,type) #at this time list_1 has already became a set, and there is no repeated value in this set

# 取list1和list2的交集 (1,2中重复的元素)
print(list_1.intersection(list_2))
# 取list1和list2的并集 (1,2中所有的不重复元素)
print(list_1.union(list_2))
# list1和list2的差集 即在1中有的元素在2中没有 或在2中有在1中没有的元素
print(list_1.difference(list_2))
print(list_2.difference(list_1))
# 取子集 返回结果是 true 或者

print(list_1.issubset(list_2))

list_3 = set([1,2,3])
list_4 = set([1,2,3,4])
print(list_3.issubset(list_4))
print(list_4.issuperset(list_3))

# 对称差集 差集(我有你没有) 对称差集(把彼此集合中互相没有的元素取出来《属于A不属于B，和，属于B不属于A》)

print(list_3.symmetric_difference(list_4))

print(list_4.symmetric_difference(list_3))

list_5 = set([1,2,3])
list_6 = set([4,5,6])

print(list_5.isdisjoint(list_6))
print(list_3.isdisjoint(list_4))