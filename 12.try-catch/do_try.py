
# -*- coding: utf-8 -*-

import logging
import sys

try:
    raise ValueError('A very specific bad thing happened.')
except:
    logging.error("Unexpected error: {}".format(sys.exc_info()))