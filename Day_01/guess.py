#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo
# 多条件判断分支
age_of_oldboy = 27

guess_age = int(input("plz guess the age of duo"))

if guess_age == age_of_oldboy:
    print("OMG you got it")
elif guess_age > age_of_oldboy:
    print("give me a smaller age")
else:
    print("give me a bigger one")
