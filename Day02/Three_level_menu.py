#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

menu = {
    'United States':{
        'State of Wisconsin':{
            'Milwaukee':['Marquette University','UWM-Milwaukee'],
            'Midsion':['first university','second university']
        },
        'State of California':{
            'Los Angeles':['LA-University1','LA-University2']
        }
    },
    'Peoples Republic of China':{
        'Liaoning Provence':{
           'Dalian': ['Neusoft University','Dalian Marine University']
        },
        'Beijing':{
            'zhongguancun':['bunch of idiot','iam one of the idiot']
        }
    }
}

while True:
    for i in menu:
        print(i)
    choice = input(">>>>choice a submenu to enter")
    if choice in menu:
        while True:
            for i2 in menu[choice]:
                print("\t",i2)
            choice2 = input(">>>>choice a submenu to enter")
            while True:
                for i3 in menu[choice][choice2]:
                    print("\t\t",i3)
                choice3 = input(">>>>choice a submenu to enter")
                for i4 in menu[choice][choice2][choice3]:
                    print("\t\t\t",i4)
                break
            break
        break



