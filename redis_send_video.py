#!/usr/bin/env python3

import cv2
import struct
import redis
import numpy as np
import time

def toRedis(r, img, key):
    """Store given Numpy array 'a' in Redis under key 'n'"""
    h, w = img.shape[:2]
    shape = struct.pack('>II',h,w)
    encoded = shape + img.tobytes()

    # Store encoded data in Redis
    r.set(key, encoded)
    return

if __name__ == '__main__':

    # Redis connection
    r = redis.Redis(host='localhost', port=6379, db=0)
    cam = cv2.VideoCapture('w.mp4')

    while True:
        ret, img = cam.read()
        
        if ret is True:
            #cv2.imshow('img', img)
            toRedis(r, img, 'image')
            print("send picture")
        else:
            print("video is off")
            exit()
        time.sleep(0.01)