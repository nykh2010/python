# -*- coding: utf-8 -*-
"""
Created on Sat May 12 15:18:49 2018

@author: Administrator
"""

import hashlib

def hashStr(strInfo):
    """
    对字符串进行hash
    """
    h = hashlib.md5()  #使用md5,
    h.update(strInfo.encode("utf-8")) #对一段进行utf8编码的字符串进行hash
    return h.hexdigest()
 
BUFSIZE = 2048    
def hashFile(fileName):
    """
    对文件进行hash
    """
    try:
        f = open(fileName,'rb')
    except IOError:
        return None
    h = hashlib.md5()
    while True:
        chunk = f.read(BUFSIZE)
        if not chunk:
            break
        h.update(chunk)
    f.close()
    return h.hexdigest()

print(hashStr("hello"))
print(hashFile("C:/Users/Administrator/Desktop/网络爬虫/VIP班/第二天/note.txt"))  

    