#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

import csv
import json
import sys

def trans(path):
    jsonData=open(path+'.json')
    #csvfile = open(path+'.csv', 'w')#
    #csvfile = open(path+'.csv', 'wb')# below is for python2
    csvfile = open(path+'.csv', 'w',newline='')# below is for python3
    for line in jsonData:#获取属性列表
        dic=json.loads(line[0:-2])
        keys=dic.keys()
        break
    writer = csv.writer(csvfile)
    writer.writerow(keys)#
    for dic in jsonData:#
        dic=json.loads(dic[0:-2])
        writer.writerow(dic.values())
    jsonData.close()
    csvfile.close()

if __name__ == '__main__':
    path=str(sys.argv[1])#获取path参数
    print (path)
    trans(path)