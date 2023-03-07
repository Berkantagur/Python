#NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides 
# a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of 
# routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, 
# I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

"""
a = [1, 2, 3, 4, 5, 6]
b = [2, 4, 5, 8, 9, 7]
ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])
print(ab)
"""
                                                                                                                                                                 
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([2, 4, 5, 8, 9, 7])
print(a * b) 
