#Reshaping means changing the shape of an array.
#The shape of an array is the number of elements in each dimension.
#By reshaping we can add or remove dimensions or change number of elements in each dimension.

import numpy as np

print(np.random.randint(1, 10, size=9))
print(np.random.randint(1, 10, size=9).reshape(3,3))

ar = np.random.randint(1, 10, size=9)
print(ar.reshape(3,3))