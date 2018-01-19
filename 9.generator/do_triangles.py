# -*- coding: utf-8 -*-


def triangles1():
    l = [1]
    while True:
        yield l
        l = [sum(x) for x in zip([0]+l, l+[0])]



n = 0
for t in triangles1():
    print(t)
    n = n + 1
    if n == 10:
        break;


num = 10;
list1 = [1]

for i in range(1, 11):
    print(list1)
    list1 = [1] + [x + y for x,y in zip(list1[:], list1[1:0])] + [1]

