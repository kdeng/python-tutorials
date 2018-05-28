"""
the first demo to do multi-threading in Python
"""

import time, threading, random

def loop():
    print('thread %s is runing ...' % threading.current_thread().name)
    n = 0

    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(random.random())

    print('thread %s ended.' % threading.current_thread().name)

t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)
