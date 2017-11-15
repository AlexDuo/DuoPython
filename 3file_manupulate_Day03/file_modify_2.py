#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 修改一个文件的思路，打开一个文件，修改，然后存入另一个

f = open('sbchickensoup','r',encoding='utf-8')

f_new = open('sbchickensoup2','w',encoding='utf-8')

for line in f:
    if '你的价值远比你想象的高' in line:
        line = line.replace('你的价值','你的人生目标')
    f_new.write(line)
f.close()
f_new.close()
