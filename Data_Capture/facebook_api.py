#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo


import facebook
import json
# a new comment
# Get the token and access into the data
graph = facebook.GraphAPI(access_token='EAACEdEose0cBAMGvZBEmBin4ZBquSVKzQZBVWreBiPwDPwn2ETyxozkZBUblQMt88mCw3B46Ws3ZCrKQ5OmKignOuxzeZAAWUlRSeMIJHfZBYtaaL1p9yFo86eWeinDT7xqfiRwDHzWb5J33EuRwLeyVkm5cTDF6vnQB841tBUDFxztpQgjzM9LItMGmFY3fiVhPeYM371xsgZDZD')

# call the get_object method ('whose info me&id' fields(multiple) or field(single))
info = graph.get_object('me',fields = 'age_range,name,location{location},devices')

# get_connections could get the related info about someone
likes = graph.get_connections('me', connection_name='likes')
# the info and likes are dictionaries, they are disordered. I used the attribute ensure_ascii = False because
# there are Chinese character in my data (my name) and at the first fo the code I set up the character Encoding as
# utf-8
json.dump(info,open('C:/Users/Real/Desktop/result.json','w'),ensure_ascii= False)
json.dump(likes,open('C:/Users/Real/Desktop/result_likes.json','w'),ensure_ascii= False)
print(info)
print(likes)
