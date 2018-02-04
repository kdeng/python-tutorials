from functools import reduce

def add(x, y):
    return x + y

r = reduce(add, range(0, 10))

print(r)


def join(x, y):
    return x + y

r = reduce(join, map(str, range(0, 10)))

print(r)