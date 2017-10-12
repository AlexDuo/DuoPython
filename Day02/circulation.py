#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

name = ["one","two","three","four","five","six"]
# List traversal
# for i in name:
#     print(i)
# [start index: end index : step length]
print(name[0:-1:2])
# we can omit the first and the last index which means 0 and -1
# Therefore, to traversal the list is  list_name[:]  first index to last index (already omitted)
print(name[:])