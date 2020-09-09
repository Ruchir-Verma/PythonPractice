'''
Arrays are similar to list , but they store only homogenous values.
Need to import module array to use it
'''

from array import *

vals = array('i',[5,9,8,4,2])   #i represents type of array,here integer.

print(vals)


'''
To get the size of array ,use buffer_info function
'''

print(vals.buffer_info())

'''
To get the type of array,use typecode function
'''

print(vals.typecode)


'''
To reverse the array
'''

vals.reverse()
print(vals)


'''
Creating a copy of an array
'''

newArr = array(vals.typecode,(a for a in vals))
print(newArr)