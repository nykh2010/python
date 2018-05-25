import multiprocessing

def f():
  while True:
    pass

if __name__ == '__main__':
  t = multiprocessing.Process(target=f)
  t.start()

  while True:
    pass