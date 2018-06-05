#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

class DuoException(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message


try:
    raise DuoException('我的异常')

except DuoException as e:
    print(e)