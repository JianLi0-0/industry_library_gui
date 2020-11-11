#!/usr/bin/env python3

#import cv2
from time import sleep
import struct
import redis
import numpy as np

def fromRedis(r,n):
    """Retrieve Numpy array from Redis key 'n'"""
    encoded = r.get(n)
    h, w = struct.unpack('>II',encoded[:8])
    a = np.frombuffer(encoded, dtype=np.uint8, offset=8).reshape(h,w,3)
    return a

if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, db=0)
    img = fromRedis(r,'image')
    if img is None:
        exit()
    #print(f"read image with shape {img.shape}")
