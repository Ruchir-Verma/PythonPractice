'''
Numpy arrays can be used to create multi dimesional arrays in python.

When we create an array using Numpy , we do not need to specify the type of it
'''

from numpy import *

arr = array([1,2,3,4,5])
print(arr)


'''
Ways of creating a numpy array:

arrays()
linspace()
logspace()
arange()
ones()
zeroes()

'''

#dtype can be used  to check the datatype of an array

x=array([1,2,3,4,5])
print(x.dtype)

'''
If any element in an array is of different data type which consumes more memory, then data type of that array will be of
that particular type.    ----> Implicir Conversion
'''

x = array([1,2,3,4,5.5])
print(x)
print(x.dtype)


'''
Linespace takes three inputs , start point,end point , number of divisions between start  point  and end point.

If we do not specify number of divisions , we always get 50 divisions

Always has float data type
'''

x = linspace(1,20,10)
print(x)

x = linspace(1,20)
print(x)


'''
arange can be used to create an array , which takes 3 inputs.

Start point ,end point , steps to skip
'''

x = arange(1,20,2)
print(x)

'''
zeros() and ones() can be used to create an array with all the elements as zeros and ones respectively. They take the 
argument size of the array.

'''

x = zeros(5)
print(x)

y = ones(5)
print(y)

