# -*- coding: utf-8 -*-
"""
Created on Sun May 20 10:02:13 2018

@author: Administrator
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://www.bing.com")
time.sleep(5)

# 打开bing搜索，搜索区块链
for i in range(10):
    try:
        driver.find_element_by_id('sb_form_q').send_keys('区块链') 
        driver.find_element_by_id('sb_form_go').click()
        break
    except:
        time.sleep(1)
        
# 有道翻译
driver.get("http://fanyi.youdao.com/")
time.sleep(5)
for i in range(10):
    try:
        driver.find_element_by_id('inputOriginal').send_keys('hello')
    except:
        time.sleep(1)
driver.quit()
driver.close()

