### Normal function
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    print('done')

fib1(10)


### Define a function to instantiate generator
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    print('done')

### This is a function
print('fib2:', fib2)

### This is a generator
print('fib2(10):', fib2(10))
