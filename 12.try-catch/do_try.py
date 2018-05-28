
# -*- coding: utf-8 -*-

import logging
import sys



def some_func():
    raise ValueError('A very specific bad thing happened.')

try:
    some_func()
except:
    # logging.error("Unexpected error: {}".format(".".join(sys.exc_info())))
    print(sys.exc_info())