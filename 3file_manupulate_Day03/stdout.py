#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 实现标准输出（非换行输出，例如安装进度条）

import sys,time

for i in range(20):
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.5)