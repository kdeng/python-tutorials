"""
communicate between two processes by using queue
"""

from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print('Process to write :%s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue ...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        print("Trying to get from queue.")
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ =='__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()

    # waiting for write process to complete
    pw.join()
    pr.terminate()