#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

import os
import json
import facebook

if __name__ =='__main__':
    # set the token as a environment variable named FACEBOOK_TEMP_TOKEN
    # and then use os.environ.get to get the token and send the token into GraphAPI
    token = os.environ.get('FACEBOOK_TEMP_TOKEN')

    graph = facebook.GraphAPI(token)

    profile = graph.get_object('me', field='name,location')

    print(json.dump(profile, indent=4))

