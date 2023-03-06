dictionary = {'a': 4,
              'b': 3,
              'c': 6,
              'd': 9,
              'e': 7}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

x = {k: v**2 for (k,v) in dictionary.items()}
print(x)

y = {k.upper(): v for (k,v) in dictionary.items()}
print(y)

z = {k.upper(): v*3 for (k,v) in dictionary.items()}
print(z)