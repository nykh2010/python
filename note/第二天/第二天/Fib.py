# -*- coding: utf-8 -*-
"""
Created on Sat May 12 09:35:36 2018

@author: Administrator
"""

#F(n) = F(n-1)+F(n-2) n >= 2
#       1             0 <= n < 2, n Belongs to N

def F(n):
#    if type(n) != type(1) or n < 0:
#        print("Invaild Input")
#        return None
    if n < 2:
        return 1
    else:
        return F(n-1)+F(n-2)
            
def F2(n):
    x,a,b=0,0,1
    while x < n:
        a,b = b,a+b
        x += 1
    return b

for i in range(100):
    print(F2(i))
    
    
