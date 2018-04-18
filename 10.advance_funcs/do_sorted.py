
# -*- coding: utf-8 -*-

from operator import itemgetter

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t

L2 = sorted(L, key=by_name)
# print(L2)


# def by_score(s):
#     return 

# L3 = sorted(L, key=by_score)
# print(L3)

print(sorted(L, key=itemgetter(0)))
# print(sorted(L, key=lambda t: t[1]))
# print(sorted(L, key=itemgetter(1), reverse=True))