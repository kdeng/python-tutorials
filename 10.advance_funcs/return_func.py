
# -*- coding: utf-8 -*-

def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

def count1():
    def l(j):
        return lambda: j * j
    fs = []
    for i in range(1, 4):
        fs.append(l(i))
    return fs


f1, f2, f3 = count()

print("f1:", f1)
print("f2:", f2)
print("f3:", f3)


print("f1():", f1())
print("f2():", f2())
print("f3():", f3())


