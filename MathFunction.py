'''
Math is an inbuilt function that provides various useful in-built  methods to perform certain operations
'''

import math as m

''' to find squareroot of a number'''
x = m.sqrt(25)
print(x)

''' to find floor and ceil values'''

print(m.floor(2.4))
print(m.ceil(2.4))

''' to perform factorials'''

print(m.factorial(5))

''' to perform trignometric operations'''

print(m.sin(5))

''' to perform power '''

print(m.pow(2,3))

''' There are some in-buit constatnts as well in python '''

print(m.pi)
print(m.e)

''' If we want to import only some specific methods , use as following :

from math import pow,sqrt
pow(2,3)   --- > returns 8
sqrt(4)    --- > returns 2

'''