import threading
import os

ROOT_PATH = "C:\\Users\\xulingfeng\\Documents\\"
ROOT_NAME = "Tencent Files"
DST_PATH = "D:\\"
search_path = []
copy_path = []
thread_list = []
copy_thread_list = []

copy_path_mutex = threading.Lock()
search_path_mutex = threading.Lock()

def copy_to_dst_path(copy_path):
	global copy_path_mutex
	while copy_path != []:
		try:
			copy_path_mutex.acquire()
			dir = copy_path.pop()
			copy_path_mutex.release()
			src_file = open(dir,'rb')
		except FileNotFoundError:
			print(dir+" not found")
			continue
		except IndexError:
			break
		dst_file = open(DST_PATH+dir,'wb')
		print("open "+DST_PATH+dir)
		flag = True
		while flag:
			try:
				buf = src_file.read(4096)
				dst_file.write(buf)
				if len(buf) < 4096:
					raise EOFError
			except EOFError:
				src_file.close()
				dst_file.close()
				print("close "+DST_PATH+dir)
				flag = False				

def get_from_search_path(search_path,copy_path):
	search_path_mutex.acquire()
	dir = search_path.pop()
	if not os.path.exists(DST_PATH+dir):
		os.mkdir(DST_PATH+dir)
	search_path_mutex.release()
	listdirs = os.listdir(ROOT_PATH+dir)
	print(listdirs)
	for listdir in listdirs:
		new_path = dir + '\\' + listdir
		print(new_path)
		if os.path.isdir(ROOT_PATH+dir+'\\'+listdir):
			search_path_mutex.acquire()
			search_path.append(new_path)
			search_path_mutex.release()
		else:
			copy_path_mutex.acquire()
			copy_path.append(new_path)
			copy_path_mutex.release()
		# print(listdir)
		# pass

def main():
	os.chdir(ROOT_PATH)
	# os.mkdir(DST_PATH)
	print(os.listdir())
	search_path.append(ROOT_NAME)
	while True:
		if search_path == []:
			break
		else:
			thread_count = len(search_path)
			# print(thread_count)
			for i in range(thread_count):
				main_thread = threading.Thread(target=get_from_search_path,args=(search_path,copy_path))
				thread_list.append(main_thread)
				main_thread.start()
			for thread in thread_list:
				thread.join()
	for i in range(10):
		copy_thread = threading.Thread(target=copy_to_dst_path,args=(copy_path,))
		copy_thread_list.append(copy_thread)
		copy_thread.start()
	for thread in copy_thread_list:
		thread.join()

	# print(search_path)
	# print(copy_path)
	print(len(copy_path))


if __name__ == '__main__':
	main()