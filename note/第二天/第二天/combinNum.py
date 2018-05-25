# -*- coding: utf-8 -*-
"""
Created on Sat May 12 13:42:04 2018

@author: Administrator
"""

def CombNum(m, n):
    if n==0 or m==n:
        return 1
    return CombNum(m-1,n)+CombNum(m-1,n-1)


print(CombNum(3,1))
print(CombNum(3,2))
print(CombNum(5,3))



