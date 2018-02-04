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

def triangles2(n):
    l = [1]
    while n > 0:
        yield l
        l = [1] + [x + y for x, y in zip(l[:], l[1:0])] + [1]
        n -= 1
    return

print("triangles2")

n = 0
for t in triangles2(10):
    print(t)
    n = n + 1
    if n == 10:
        break

