'''

We do not have concept of Abstract classes in python , but it can be achieved by ABC module,which is Abstract Base Classes.


Method which just have declaration and do not have definition is called as abstract method and class which has abstract method
is a abstract class.

We cant make object of an abstract class

'''

from abc import ABC,abstractmethod

class A(ABC):

    @abstractmethod
    def show(self):
       pass
                                                         #We can call show() with object of A,since it is an abstract class.


class B(A) :
                                                       #If we put pass in B , it will again not call the show(),as we need to define B,
                                                       #else it would be abstract as well.
    def show(self):
        print("This is Running")


b = B()
b.show()