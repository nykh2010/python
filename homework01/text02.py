# -*- coding: utf-8 -*-
'''
    有一个文件夹，下面有1000+文件。把这个文件夹中的所有文件拷贝到另一个文件夹下：
    要求：使用多进程（多线程）或进程池（线程池）；使用Hash证明文件完整性
'''
import threading
import os

PATH = "H:\Redirect\Documents"

SRC_FOLDER_PATH = "Source Insight 4.0\\"
DST_FOLDER_PATH = "Source Insight 4.0 BACKUP\\"

def file_list(path):
    pass

def move(dst,src):
    pass
    
if __name__ == '__main__':
    os.chdir(PATH)
    try:
        os.mkdir(DST_FOLDER_PATH)
    except FileExistsError:
        print(DST_FOLDER_PATH,"exist")
#    os.chdir(PATH+SRC_FOLDER_PATH)
    files = os.listdir(SRC_FOLDER_PATH)
#    print(files)
    for file in files:
        print(file)
        if os.path.isdir(SRC_FOLDER_PATH+file):
            print(DST_FOLDER_PATH+file)
            try:
                os.mkdir(DST_FOLDER_PATH+file)
            except FileExistsError:
                continue
        else:
            try:
                src_file = open(SRC_FOLDER_PATH+file,"rb")
            except:
                print("open failed:"+file)
                continue
            try:
                dst_file = open(DST_FOLDER_PATH+file,"a")
            except FileExistsError:
                print("file exist:"+file)
            dst_file.close()
            src_file.close()