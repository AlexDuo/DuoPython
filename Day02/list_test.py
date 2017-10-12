#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# this test prove that:
# when we trying to copy a list which have a sublist, we will only copy the memory address of it, but not the attribute of it.
# therefore, when we modify the sublist value in the duplicate list, the origin list will also change.
import copy
name = ["one","two","three",["3.0","3.5"],"four","five"]

name1 = name.copy()

name1[3][0] = "three_point_o"

print(name)
print(name1)

# when we define a variable equals to another variable, it means the two variable are point at the same memory address.
name = name1

# we got another method called depcopy, that will copy all the things, that means after doing the depcopy the two variables
# are independent to each other, but before we do that, we have to import the package of copy

name1 = copy.deepcopy(name)