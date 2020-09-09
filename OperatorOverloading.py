'''

Operator overloading means to use the opertor tp perform certain operations which are not pre-defined in python.

Example :

when we perform (5+4) ,or ('ruchir'+'verma') , it internally calls a predefined method __add__ which takes two parameters
and perform addition(of integers) or concatenation(of strings).

Suppose we want to add two objects ,

s1 = Student(marks1,marks2)
s2 = Student(marks3,marks4)

s3 = s1+s2   #It will give error.

To do this we have to overload the __add__ method like below :

'''

class A:

    def __init__(self,marks1,marks2):

       self.marks1=marks1
       self.marks2=marks2

    def __add__(self, other):

        marks1 = self.marks1+other.marks1
        marks2 = self.marks2+other.marks2
        result = A(marks1,marks2)
        return result



s1 = A(40,50)
s2 = A(20,40)

s3 = s1+s2
print(s3.marks1)