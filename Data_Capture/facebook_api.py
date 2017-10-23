#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo


import facebook
import json
# a new comment
# Get the token and access into the data
graph = facebook.GraphAPI(access_token='EAACEdEose0cBAPaAYONlj7ZCeeffsctuAUX4VCoC8wS25mLVf6VHdFAz82wa61jIzZBX0gp2bQNQTS8ZBDIqyBzpQ3hWw2cb1sqGbFuCoJfNZBSBhVyMZA5OQfeUBtZB5lRUyH7NxyjFvuaNIX6gRFUM6WCroH9c2vu1VqKK4Jc2bKcPehJi8fe8q5bEGrWJzuZCJBwTSp6iQZDZD')

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
