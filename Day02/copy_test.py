#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

import copy

name1 = []
# 这样就完成了一个浅copy 以下是浅copy的三种方式
p1 = copy.copy(name1)

p2 = name1[:]

p3 = list(name1)
# 浅copy的用途可以是 用浅copy 生成两个variable 后他们中的sublist可以作为公用内容 例如夫妻二人同来自于人的类型，他们的saving
# 是共享的, modify 其中一个人的saving 可以引起两个人共同的变化，因为sublist的copy是指向内存地址的。
person = ["name",["saving",100]]

person1 = person[:]
person2 = person[:]

person1[0]="Alex"

person2[0]="Yang"

person1[1][1]=50
print(person1)
print(person2)
