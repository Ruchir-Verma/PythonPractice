'''

Recursion is calling a function from itself.

Maximum limit  is 1000 , i.e. , a function can call maximum 1000 times ,itself
'''

#To get the limit of recursion, use getrecursionlimit function.

import sys
print(sys.getrecursionlimit())  #returns 1000


#To change the limit,use setrecursionlimit function

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
def fun():
    print ("Hello")
    fun()


fun()
