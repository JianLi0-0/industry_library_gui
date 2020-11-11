#!/usr/bin/env python3

import redis
import json
import time

width = 80
height = 200
x_i = width+80
fx = 50
fy = 100

dict = {'object_0': {'bounding_box':[fx, fy, fx+width, fy+height], # [x1, y1, x2, y2]
                     'position': [1, 10, 100]}, 
        'object_2': {'bounding_box':[fx+x_i, fy, fx+x_i+width, fy+height],
                     'position': [1, 10, 100]}, 
        'object_3': {'bounding_box':[fx+x_i*2, fy, fx+x_i*2+width, fy+height],
                     'position': [1, 10, 100]}}

dict1 = {'object_1': {'bounding_box':[fx, fy, fx+width, fy+height], # [x1, y1, x2, y2]
                     'position': [1, 10, 100]}, 
        'object_2': {'bounding_box':[fx+x_i, fy, fx+x_i+width, fy+height],
                     'position': [1, 10, 100]}, 
        'object_3': {'bounding_box':[fx+x_i*2, fy, fx+x_i*2+width, fy+height],
                     'position': [1, 10, 100]}}

if __name__ == '__main__':
    
    pool = redis.ConnectionPool(host='127.0.0.1',port=6379)
    r = redis.Redis(connection_pool=pool)

    while True:
        r.hset('object_list', 'one', json.dumps(dict))
        time.sleep(1)
        r.hset('object_list', 'one', json.dumps(dict1))
        time.sleep(1)        

    
        