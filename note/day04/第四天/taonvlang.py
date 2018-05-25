# -*- coding: utf-8 -*-
"""
Created on Sun May 20 15:32:24 2018

@author: Administrator
"""

from selenium import webdriver
import time
import os
from urllib.request import urlopen
import hashlib
import re

def mkdir(path):
    # 创建本地的文件夹路径
    if not os.path.exists(path):
       os.makedirs(path)
       print(path,"已经创建")
       
def hashStr(strInfo):
    """
    对字符串hash
    """
    h = hashlib.sha256()
    h.update(strInfo.encode("utf-8"))
    return h.hexdigest()
    
# url来自：详情页里面html进行一个<img[\s\S]*?src="([\s\S]*?)" 正则的匹配       
def savePic(url, localPath):
    """
    根据当前时间的hash值来保存图片
    """
    data = urlopen(url).read()
    with open(localPath+'/'+hashStr(time.ctime())+'.jpg', 'wb') as f:
        f.write(data)

#savePic("http://img.alicdn.com/imgextra/i4/2926567173/TB1uXrgLXXXXXbYXpXXXXXXXXXX_!!0-tstar.jpg_620x10000.jpg", "C:\\Users\\Administrator\\Desktop\\网络爬虫\\VIP班\\第四天")

url = "https://mm.taobao.com/search_tstar_model.htm?"
driver = webdriver.Chrome()

driver.get(url)
time.sleep(2)

pattern = re.compile('<li class="item">[\s\S]*?<a href="([\s\S]*?)"[\s\S]*?<span class="name">([\s\S]*?)</span>[\s\S]*?<span class="city">([\s\S]*?)</span>')
girlsInfo = re.findall(pattern, driver.page_source)
for it in girlsInfo: # it[0] --> 详情url，
                     # it[1] --> 姓名，
                     # item[2] --> 所在城市
    # print(it[0],it[1],it[2])
    pattern = re.compile('([1-9]\d*)$')
    girlsid = re.findall(pattern, it[0])
    # print(girlsid)
    mkdir(girlsid[0] + ' ' + it[1] + ' ' + it[2])
    
    detail_page = urlopen(it[0]).read()
#with open("taonvlang.html", "wb") as f:
#    f.write(driver.page_source.encode("utf-8"))
    
#<li class="item">[\s\S]*?<a href="([\s\S]*?)"[\s\S]*?<span class="name">([\s\S]*?)</span>[\s\S]*?<span class="city">([\s\S]*?)</span>


# 进详情页，获取一个个真正的图片url <img[\s\S]*?src="([\s\S]*?)"
# 使用savePic将一张张图片存到本地;