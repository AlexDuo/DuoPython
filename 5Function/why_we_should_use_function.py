#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 代码的重复利用，同能内容写进函数，调用函数多次执行
# 使用函数三大优点：1.提高代码复用性。 2.保持一致性。 3.可扩展性
import time
def write_a_line():
    time_format = '%Y-%M-%D %X'
    time_current = time.strftime(time_format)
    with open('test.txt','a+') as f:
        f.write('%s write a new record at the end of the file\n' %time_current)


# write_a_line()
# time.sleep(10)
# write_a_line()
# time.sleep(10)
# write_a_line()

for i in  range(3):
    write_a_line()
    time.sleep(5)