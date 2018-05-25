# -*- coding: utf-8 -*-
"""
Created on Sun May 20 13:33:07 2018

@author: Administrator
"""
import os
from multiprocessing import Pool,Manager
import hashlib

CHUCKSIZE = 2048
def hashFile(fileName):
    """
    对文件进行hash，并且返回一个16进制字符串信息
    """
    h = hashlib.md5()
    # 打开文件
    with open(fileName, 'rb') as f:
        while True:
            chunk = f.read(CHUCKSIZE)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def copyFile(fileName, srcPath, destPath, q):
    """
    拷贝文件的操作
    """
    # 1.srcPath不存在，报错
    if not os.path.exists(srcPath):
        print("srcPath %s is not exist"%srcPath)
        return False
    
    # 2.destFile存在，提示是否覆盖
    # destPath不存在，则创建
    if not os.path.exists(destPath):
        try:
            os.mkdir(destPath)
        except:
            print("mkdir %s error"%destPath)
            return False
    
    srcFileName = srcPath+'/'+fileName
    destFileName = destPath+'/'+fileName
    # Note:需要使用二进制字节的方式来读写文件
    with open(srcFileName, 'rb') as fr:
        with open(destFileName, 'wb') as fw:
            for i in fr:
                fw.write(i)
    
    q.put(fileName) # 通知主进程当前这个文件拷贝完毕
    return True

if __name__ == "__main__":
    srcPath = input("请输入您要拷贝的文件目录:")
    desPath = srcPath+'-副本'
    #C:\Users\Administrator\Desktop\网络爬虫\VIP班\第四天\Note.txt
    
    while os.path.isdir(desPath):
        desPath = desPath+'-副本'
    
    fileList = os.listdir(srcPath)
    fileNum = len(fileList)
    num = 0# 用于记录当前拷贝了多少个文件，从而来判断进度
    # 即使拷贝出错了，进度也得加一
    
    # 进程池
    p = Pool()
    q = Manager().Queue()  # 进程池之间交互数据，得用进程池的队列
    for i in fileList:
        p.apply_async(func=copyFile, 
                      args=(i, srcPath, desPath, q))
    p.close()
    
    while num < fileNum:
        #主进程进行对完成拷贝的文件进行hash检测
        fileName = q.get() # 主进程get到队列中的信息
        
        # 做hash检测
        srcFileName = srcPath+'/'+fileName
        destFileName = desPath+'/'+fileName
        if (hashFile(srcFileName) == hashFile(destFileName)):
            print("%s copied ok"%srcFileName)
        else:
            print("%s copied failed"%srcFileName)
        
        # 一个新的文件被拷贝完
        num += 1
        rate = num/fileNum*100
        print("Current rate is %.lf%%"%rate)
        
    p.join()
    print("Copy Files Done")
    
    
#C:/Users/Administrator/Desktop/网络爬虫/VIP班/testCopyFiles    
#    for i in fileList:
#        copyFile(i,srcPath,desPath)
#        print(hashFile(srcPath+'/'+i))
#        print(hashFile(desPath+'/'+i))
#copyFile(srcPath,desPath)