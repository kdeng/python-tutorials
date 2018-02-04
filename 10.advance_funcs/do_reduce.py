from functools import reduce

def str2float(s):
    point = 0
    def fn(x, y):
        nonlocal point
        if (y == -1):
            point = 1
            return x
        elif point == 0:
            return x * 10 + y
        else:
            point = point * 10
            return x + y / point
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': -1}[s]
    return reduce(fn, map(char2num, s))

print('str2float(\'123.456\') =', str2float('123.456'))
