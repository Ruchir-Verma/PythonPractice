'''

User defined arrays

'''
from array import *

arr = array('i',[])
n = int(input("Enter size of an array"))

for i in range(n):
    x = int(input("Enter element"))

    arr.append(x)


print(arr)


x = int(input("Enter value to be searched from array"))

for i in arr:
    if i==x:
        print("Found")
        break

else:
    print("Not found")
