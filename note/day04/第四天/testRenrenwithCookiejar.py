# -*- coding: utf-8 -*-
"""
Created on Sun May 20 11:29:56 2018

@author: Administrator
"""

# 使用cookiejar来管理cookie，可维护性
from http import cookiejar
from urllib import request
from urllib import parse

# 创建一个cookiejar对象，用来管理cookie
cookie = cookiejar.CookieJar()

# 通过HTTP Cookie Processor来处理cookie
cookie_hanlder = request.HTTPCookieProcessor(cookie)

# 构建一个opener
opener = request.build_opener(cookie_hanlder)
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')]

# 登录人人
urlLogin = "http://www.renren.com/"

data = {"email":"XXX","password":"YYY"}

# urlencode
data = bytes(parse.urlencode(data),encoding="utf-8")
# post
req = request.Request(urlLogin,data=data,method="POST")
response = opener.open(req)

reponsemyRenren = opener.open("http://www.renren.com/961482489/profile")
with open("myRenren.html","wb") as f:
    f.write(reponsemyRenren.read())


