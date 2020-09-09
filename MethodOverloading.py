'''
Technically there is no concept of method overloading in python,but we can still achieve it.

'''

class A :

    def add(self,a=None,b=None,c=None):

         if(a!=None and b!=None and c!=None):
             return a+b+c
         elif(a!=None and b!=None):
             return a+b
         else:
             return a

a = A()
x = a.add(2)   #we can pass either one or two or three argments,hence it is method overloading.
print(x)

