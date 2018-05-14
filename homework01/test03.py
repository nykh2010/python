# -*- coding: utf-8 -*-
'''无序列表去重'''
lists = [1,2,2,1,4,6,8,6,7,8,8,9,0,2,3,5]

def fun1():
    print(set(lists))

def fun2():
    for l in lists:
        while lists.count(l) > 1:
            lists.remove(l)
    print(lists)
    
def fun3():
    lists.sort()
    print(lists)

fun1()
#fun2()
fun3()