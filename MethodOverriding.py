'''
In inherience , if child class and parent class,both has same method, then while calling the method by object of child class
, child method will be called.If method is not present in child class,parent method will be called.


'''

class A:

    def show(self):
        print("This is A")


class B(A):

    def show(self):
        print("This is B")

b = B()
b.show()