# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def Han(n, a, b, c):
    """
    汉诺塔程序的实现
    """
    if n == 1:
        print(a,"move -->", c)
        return
    else:
        Han(n-1, a, c, b)
        Han(1, a, b, c)
        Han(n-1, b, a, c)
        
Han(3, 'A', 'B', 'C')

#if n <=1 : Fab(n) = 1
#Fab(n) = Fab(n-1)+Fab(n-2)
        