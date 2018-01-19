L = list(range(100))

print('L[1:7:5]:', L[:7:5])

L1 = ['Hello', 'World', 18, 'Apple', None]

print('L2:', [x for x in L1 if isinstance(x, str)])