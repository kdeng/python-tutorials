#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s(): ' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

def log2(func):
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        print('args: {}'.format(args))
        return func(*args, **kw)
    return wrapper

def log3(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__)) 
            return func(*args, **kw)
        return wrapper
    return decorator

def log4(func):
    print('before call 1')
    def wrapper(*arg, **kw):
        print('after call 1')
        output = func(*arg, **kw)
        print('after call 2')
        return output
    print('before call 2')
    return wrapper

def log5(text = None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*arg, **kw):
            output = func(*arg, **kw)
            print("after call %s " % text)
            return output
        print("before call %s" % text)
        return wrapper
    return decorator


#@log('execute')
# @log2
# @log3('invoke')
@log5()
def now(*kw):
    print("message: 2018-03-22")





now(1,2,3,4,5)
print(now.__name__)