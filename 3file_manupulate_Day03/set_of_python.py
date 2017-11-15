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
list_7 = set([1,2,3,4,5])
list_8 = set([4,5,6,7,8])

print(list_5.isdisjoint(list_6))
print(list_3.isdisjoint(list_4))
# 这个做法和intersection是一样的，取交集
print(list_1 & list_2)
# 并集
print(list_5 | list_6)
# 差集
print(list_7 - list_8)
print(list_8 - list_7)
# 对称差集
print(list_7 ^ list_8)

list_8.add(9)
print(list_8)
list_8.update([10,11,12])
print(list_8)
list_a = set([1,1,2,3,4])
# 删除某项元素
list_a.remove(1)
print(list_a)
print(len(list_a))

print(3 in list_a)
print(1 not in list_a)

print(list_a.pop())
print(list_a)
# 从这里可以看出remove he discard的结果是一样的，都是删除指定值
list_b = set([2,3,4,5])
list_b.remove(5)
print(list_b)
list_b.discard(6)
print(list_b)
# list_b.remove(9) 这里指出了 remove和discard的却别，discard指定要删除的值不在集合内的时候，不作为，当调用remove删除
# 指定值时，如果指定值不在集合内则报错。