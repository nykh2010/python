# -*- coding: utf-8 -*-
#使用一个User-Agent池（至少10个UA），打印当前的UA。每隔两秒向新浪服务器发送一次请求
#持续一分钟。获取当前页面信息，并把返回结果写到本地文件。
import requests
import random
import time
import threading

flag=1

class Thread1(threading.Thread):
    def __init__(self,ualist):
        threading.Thread.__init__(self)
        self.ualist = ualist
        self._initialized = True
    def run(self):
        global flag
        print("enter thread1")
        max = len(self.ualist)
        while(flag):
            n = random.randint(0,max-1)
            current_ua = self.ualist[n]
            '''发送一次请求'''
            headers = {'User-agent':current_ua}
            html = requests.get("http://www.sina.com.cn",headers)
            #print("thread1"+str(flag)+","+str(n))
            print(current_ua)
            print("response:"+str(html.status_code))
            time.sleep(2)
        print("thread1 exit")

class Thread2(threading.Thread):
    def run(self):
        global flag
        #print("enter thread2")
        time.sleep(60)
        flag=0
        #print(flag)
        print("thread2 exit")

def main():
    with open('User Agent.cfg','r') as f:
        uaList = f.readlines()
    thread1 = Thread1(uaList)
    thread2 = Thread2()
    thread1.start()
    thread2.start()
    thread2.join()
    thread1.join()

if __name__ == '__main__':
	main()