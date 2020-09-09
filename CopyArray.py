from numpy import *

x = array([1,2,3,4,5])

for i in range(len(x)):
    x[i] = x[i]+5

print(x)


'''
Using numpy array
'''

x = x+100
print(x)


'''
Addition of two arrays
'''

arr1 = array([1,2,3,4,5])
arr2 = array([6,7,8,9,10])

print(arr1+arr2)


'''
We can use inbuilt function like sum,min,ax,count ,concatenate (to join two arrays) using numpy
'''

x = concatenate([arr1,arr2])
print(x)

'''
To copy an array to a new array , we can use view() and copy() function.

view() ---> for shallow copy
copy() ---> for deep copy

'''

arr1 = array([1,2,3,4,5])
arr2 = arr1.view()

print(arr2)
print(id(arr1))
print(id(arr2))