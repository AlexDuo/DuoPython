#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# requirement: you got many colleges and you want to store all the names of them, you can use list to store them

# names = "alex tom jim tim rim mom"
# below is the method to define a list
names = ["Alex","Thomas","Roland","Google"]
# how do we find an attribute from a list
# 0 is the position of the attribute in the list the position is start from 0 the position 0 is attribute "Ales"
print(names[0])
# if you want to get a part of the list, you have to define the start position: end
# position+1 (because the end position is not included in the zone)
print(names[1:3])
# when we do not know the length of the list, we use -1 to get the last attribute of the list. Similarly, if we
# want to get the second to last we just use -2 to get it.
print(names[-1])
# in this case if we want to get Roland and Google
print(names[-2:])
# with the same reason
print(names[:3])
# if we want to add an attribute into the last position of the list
names.append("Apple")
print(names)
# insert an attribute into a specific location the syntax is listname.insert(the position you want to insert, attribute)
names.insert(1,"Lily")
# replace an attribute in the list
names[2] = "Thomas_II"
print(names)
# delete an attribute in the list we could directly put the attribute which we want to delete
names.remove("Lily")
print(names)
# delete an attribute method 2
del names[2]
print(names)
# delete the last one of the list default, or you could add the position you want to delete
names.pop()
print(names)
# find the index according to the value of the attribute
print(names.index("Google"))
print(names[names.index("Google")])
# insert the "Alex_I in front of the "Alex"
names.insert(names.index("Alex"),"Alex_I")
print(names)
# find how many time that an attribute appears in a list
names.insert(0,"Alex")
print(names)
print(names.count("Alex"))
# list_name.clear() wipe up the whole list
# reverse the sequence of the list
names.reverse()
print(names)
# sort the list according to the Alphabet
names.sort()
print(names)

# extend a list into one list

names_2 = ["this","is","a","new","list"]
names.extend(names_2)
print(names)
# delete a veriable
# del names
# print(names)
# copy a existing list
names_3 = names.copy()

print(names_3)
# we can also put list into the list
names_4 = ["banana","apple","tomato",["lollipop","cheesecake"],"potato"]
print(names_4)
# if we want to rename the element in the sublist of a list eg rename lollipop to icy_lollipop
names_4 [3] [0] = "icy_lollipop"
print(names_4)
# when we have sublist in a list, the list_name.copy function will only copy the first layer of the list.