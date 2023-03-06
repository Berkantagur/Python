#Exp1
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

#Exp2: 
#Purpose: It is desired to be added to a dictionary by taking the square of even numbers.

numbers = range(21)
new_dict = {}

for n in numbers:
    
    if n % 2 == 0:
        new_dict[n] = n ** 2

print(new_dict)
#OR 
print({n: n**2 for n in numbers if n % 2 == 0})