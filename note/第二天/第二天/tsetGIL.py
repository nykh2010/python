import threading

def deadW(i):
  while True:
    pass

if __name__ == '__main__':
  p = threading.Thread(target=deadW,args(1,))

  p.start()

  while True:
    pass