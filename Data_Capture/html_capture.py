#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

from urllib import request

response = request.urlopen("http://www.baidu.com")
html = response.read()
print(html)