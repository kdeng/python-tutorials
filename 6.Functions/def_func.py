import math

def quadratic(a, b, c):
    x1 = ((-1 * b) + math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
    x2 = ((-1 * b) - math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
    return x1, x2


print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))