## Normal Fact
def fact1(n):
    if n == 1:
        return 1
    else:
        return n * fact1(n-1)

def fact2(n):
    return fact2_liter(n, 1)

def fact2_liter(number, result):
    if number == 1:
        return result
    else:
        return fact2_liter(number-1, number * result)


print('fact1(5):', fact1(5))

print('fact2(5):', fact2(5))