import threading
import os

ROOT_PATH = "H:\\Redirect\\Documents\\"
ROOT_NAME = "Source Insight 4.0"
DST_PATH = "H:\\"
search_path = []
copy_path = []
thread_list = []
copy_thread_list = []

copy_path_mutex = threading.Lock()

def copy_to_dst_path(copy_path):
    global copy_path_mutex
    while len(copy_path) != []:
        try:
            copy_path_mutex.acquire()
            file_path = copy_path.pop()
            copy_path_mutex.release()
            src_file = open(file_path,'rb')
        except FileNotFoundError:
            print(file_path+" not found")
            continue
        except IndexError:
            break
        dst_file = open(DST_PATH+file_path,'wb')
        print("open "+DST_PATH+file_path)
        flag = True
        while flag:
            try:
                buf = src_file.read(4096)
                dst_file.write(buf)
                # print(dst_file.name)
            except EOFError:
                src_file.close()
                dst_file.close()
                print("close "+DST_PATH+dir)
                flag = False

def get_from_search_path(search_path,copy_path):
    file_path = search_path.pop()
    listdirs = os.listdir(ROOT_PATH+file_path)
    print(listdirs)
    for listdir in listdirs:
        new_path = file_path + '\\' + listdir
        # print(new_path)
        if os.path.isdir(ROOT_PATH + new_path):
            os.mkdir(DST_PATH + new_path)
            search_path.append(new_path)
        else:
            copy_path.append(new_path)

def main():
    os.chdir(ROOT_PATH)
#    print(os.listdir())
    search_path.append(ROOT_NAME)
    while True:
        if search_path == []:
            break
        else:
            thread_count = len(search_path)
            for i in range(thread_count):
                main_thread = threading.Thread(target=get_from_search_path,args=(search_path,copy_path))
                thread_list.append(main_thread)
                main_thread.start()
            for thread in thread_list:
                thread.join()
    for i in range(10):
        copy_thread = threading.Thread(target=copy_to_dst_path,args=(copy_path,))
        copy_thread_list.append(thread)
        copy_thread.start()
    for thread in copy_thread_list:
        thread.join()

    print(len(copy_path))


if __name__ == '__main__':
    main()