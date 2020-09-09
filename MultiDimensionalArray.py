from numpy import *

arr1= array([

    [1,2,3],
    [4,5,6]
])

'''
ndim is used to get the dimension of an array
'''
print(arr1)
print(arr1.ndim)


'''
shape will give number of rows and columns
'''

print(arr1.shape)

'''
size will give the number of elements present in an array
'''

print(arr1.size)

'''
flatten() will convert a multi-dimensional array into a single 1-d array
'''

arr2 = arr1.flatten()
print(arr2)

'''
Using reshape() , we can get multi-dimensioanl array from a 1-d array
'''

arr3 = arr2.reshape(2,3)
print(arr3)


'''
Converting a 2D array into a matrix
'''

arr2 = array([
    [1,2,3],
    [5,6,7],
    [10,11,12]


])

mat = matrix(arr2)
print(mat)


'''
To get the diagonal elements of a matrix
'''

dig = diagonal(mat)
print(dig)

'''
    ANOTHER WAY  OF CREATING MATRICES
Multiplication of matrices
'''

m1 = matrix('1,2,3;4,5,6;7,8,9')
m2 = matrix('5,6,7;8,9,10;11,12,13')

print(m1)
print(m2)

m3 = m1 * m2
print(m3)



