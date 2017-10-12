#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo


import facebook
import json

# Get the token and access into the data
graph = facebook.GraphAPI(access_token='EAACEdEose0cBAO4P8cic2ZA0jeFdi5q4ZBbzd9RZChoR316hK0OJ1qfPM87HI4859FZAUUj0aH7Wijrrv4CjeZBZBpKxqfkjZBM4tU37t0ZBBbzsZBY4x507xonjGxKe67PfBGmppAGxwvKZBxnoE01apqTNM9307xmJDTL4nPmMJhZBf5XKXOzCx6x04oS12jDHpHQaDCiRQyyfwZDZD')

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
