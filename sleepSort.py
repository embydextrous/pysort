import threading
import time

def sleep(a, n, index):
    time.sleep(n/10.0)
    a[index[0]] = n
    index[0] += 1

def sleepSort(a):
    threads = []
    index = [0]
    for i in a:
        threads.append(threading.Thread(target=sleep, args=(a, i, index,)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

a = [9, 4, 3, 0, 8, 7, 1, 2, 6, 5, 1, 3, 4, 5, 6,1, 3, 4, 2, 3, 2, 1]
sleepSort(a)
print a

