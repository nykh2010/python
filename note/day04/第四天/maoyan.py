# -*- coding: utf-8 -*-
"""
Created on Sun May 13 15:38:41 2018

@author: Administrator
"""
from multiprocessing import Pool
import requests  #发送request请求，获取response响应；
import json
import re
import time
import random
import functools


def get_one_page(url):
    """
    抓取一页的信息
    """
    ua_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
    response = requests.get(url, headers=ua_headers)
    if response.status_code == 200:
        return response.text
    return None
    
def parese_one_page(html):
    """
    解析网页信息，获取要真正抓取的数据
    """
    # <p class="name">.*?title="([\s\S]*?)"[\s\S]*?<p class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>
    pattern = re.compile('<p class="name">.*?title="([\s\S]*?)"[\s\S]*?<p class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>')
    items = re.findall(pattern,html)
    
    for item in items:
        yield{ 
                'title':item[0].strip(),
                'actor':item[1].strip(),
                'releasetime':item[2].strip()
                }

def write_to_file(item):
    """
    将数据写入本地文件
    """
    with open("猫眼电影数据2018520.txt",'a',encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False)+'\n')

def CrawlMovieInfo(lock, offset):
    """
    抓取数据的流程
    """
    #offset = 0, 10, 20,...,90
    url = "http://maoyan.com/board/4?offset="+str(offset)
    
    html = get_one_page(url)
    for item in parese_one_page(html):
        lock.acquire()
        write_to_file(item)
        lock.release()
    #time.sleep(random.randint(1,5))
        

#for i in range(10):        
#    CrawlMovieInfo(i*10)
     
if __name__ == "__main__":
    # 用进程池来抓取数据
    from multiprocessing import Manager
    manager = Manager()
    lock = manager.Lock()
    
    # 使用函数式编程的偏函数来传递一个默认参数
    partial_CrawlMovieInfo = functools.partial(CrawlMovieInfo, lock)
    pool = Pool()
    pool.map(partial_CrawlMovieInfo, [i*10 for i in range(10)])
    pool.close()
    pool.join()    
    
    
    