# -*- coding: utf-8 -*-
import threading

search_list = []
thread_list = []

def get_one_from_search_list(search_list):
    

def searchfile(search_list):
    path = get_one_from_search_list(search_list)

if __name__ == '__main__':
    for n in range[3]:
        thread = threading.Thread(target=searchfile,name=n,args=(search_list,))
        thread_list.append(thread)
    pass