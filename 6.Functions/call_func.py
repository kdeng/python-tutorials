
def replace(s):
    s = 'a'
    print('s:', s)

s1 = 'this is a string'
replace(s1)
print('s1:', s1)



def appendEnd(list):
    list.append('end')
    l2 = list
    l2.append('end2')
    print('List:', list)

l = ['a', 'b', 'c']
print('before l: ', l)
appendEnd(l)
print('after l: ', l)

def person(name, age, *args, city, job):
    print(name, age, args, city, job)


person('Jack', 24, city='Beijing', job='Engineer')

person('Mike', 44, 1, 2, 3, city='Shanghai', job='Engineer')
