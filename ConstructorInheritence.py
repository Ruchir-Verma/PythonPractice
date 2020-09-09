class A:

    def __init__(self):
        print("Calling init A")

    def feature1(self):
        print("feature1")


class B(A):

    def feature2(self):
        print('feature2')


b = B()  #This will prinit message inside init of A , which means objects of B calls constructor of A


''''
But if we create init of B ,then it will call only init of B and not of A

'''
class C:

    def __init__(self):
        print("Calling init C")

    def feature1(self):
        print("feature1")


class D(C):

    def __init__(self):
        print("Calling init D")

    def feature2(self):
        print('feature2')

d = D ()



'''
If  we want to call init of parent as well , use super() keyword

'''

class C:

    def __init__(self):
        print("Calling init C")

    def feature1(self):
        print("feature1")


class D(C):

    def __init__(self):
        super().__init__()
        print("Calling init D")

    def feature2(self):

        print('feature2')

d = D ()



#######################################################################################################


'''
METHOD RESOLUTION ORDER


Suppose we are having a multilevel inheritence in C from A and B , then while calling the init using super() , it will
always call the init of class on left side inside parenthesis.

class C(A,B)

Using super().__init() , always A's init will be called.


Same goes for methods as well, if there are methods with same name in A and B.

'''





