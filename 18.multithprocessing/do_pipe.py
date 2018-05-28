"""
communicate between two processes by using pipe
"""

from multiprocessing import Process, Pipe
import os, random, time


def write(pipe_child_connection):
    print('Process to write :%s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Send %s to pipe ...' % value)
        pipe_child_connection.send(value)
        time.sleep(random.random())

def read(pipe_parent_connection):
    print('Process to read: %s' % os.getpid())
    while True:
        print("Trying to get from pipe.")
        value = pipe_parent_connection.recv()
        print('Get %s from pipe.' % value)


if __name__ =='__main__':
    parent_conn, child_conn = Pipe()
    pw = Process(target=write, args=(child_conn,))
    pr = Process(target=read, args=(parent_conn,))

    pw.start()
    pr.start()

    # waiting for write process to complete
    pw.join()
    pr.terminate()