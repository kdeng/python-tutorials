# -*- coding: utf-8 -*-

import pickle

d = dict(name='Bob', age=20, score=88)

print(pickle.dumps(d))

with open('out.txt', 'wb') as out:
    out.write(pickle.dumps(d))


with open('out.txt', 'rb') as input:
    d = pickle.load(input)
    print("Input file content: {}".format(d))