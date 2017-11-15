#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 值得注意的是continue的特点是跳出本次循环，继续下一次循环
# 在下面的循环中 pin 只打印了5次(i=0,1,2,3,4) 因为在 i=5的时候，
# 循环进行到else便从新进入到了下一次循环当中

for i in range(10):
    if i < 5:
        print(i)
    else:
        continue
    print("pin")