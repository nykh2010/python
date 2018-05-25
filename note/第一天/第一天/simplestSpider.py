# -*- coding: utf-8 -*-
"""
Created on Sun May  6 12:04:01 2018

@author: Administrator
"""

# 1.向web服务器发起HTTP请求，http request，
# 2.服务器返回我们需要的数据, http response;
# 3.拿到返回的数据，需要精确的提取想要的数据；
# 4.保存到本地，可以是文件系统，也可以是数据库等等；

from urllib import request
#print(request.urlopen(request.Request("http://www.baidu.com"))
#      .read())

# 构造Request
#User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36
ua_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
req = request.Request("http://www.sina.com.cn/",
                      headers=ua_headers)
reponse = request.urlopen(req).read()


with open("sina2.html", "wb") as f:
    f.write(reponse)
    


## 使用requests
#import requests
#response = requests.get("http://www.sina.com.cn")
#response.encoding = 'utf-8'
## a bytes-like object is required, not 'str'
#with open("sina.html", "wb") as f:
#      f.write(response.text.encode('utf-8'))
#print(response.text)
      
      
      














    