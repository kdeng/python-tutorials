def normalize(name):
    if isinstance(name, str):
        return name.lower().capitalize()
    else:
        return None

L1 = ['adam', 'LISA', 'barT', 123, []]
L2 = list(map(normalize, L1))
print(L2)

