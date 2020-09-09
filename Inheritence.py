'''

Inheritence is the property of accessing the parent class objects from a  child  class

'''

class A:

    def feature1(self):
        print("Feature 1")


    def feature2(self):
        print("Feature 2")


class B(A):              #Inherited class A

    def feature3(self):
        print("This is feature 3")


b = B()
b.feature1()


'''
Types of Inheitence

1. Single level =  class A , class B(A)
2. Multilevel   =  class A , class B(A), class C(B)
3. Multiple     =  class A , class B ,class C(A,B)

'''



