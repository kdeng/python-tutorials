"""
This demo shows how to use ThreadLocal under multi-thread environment
"""

import threading

# class Student(object):
    
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name

local_school = threading.local()

def process_student():
    std = local_school.student
    print("Hello, %s (in %s)" % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
