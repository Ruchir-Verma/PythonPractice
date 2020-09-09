'''

We can define innser class inside a class, but that can only be accesssed by the object of the parent class.

'''


class Student:

    def __init__(self,name,age):

        self.name = name
        self.age  = age
        self.lap = self.Laptop()

    def show(self):

        print(self.name , self.age )
        self.lap.show()

    class Laptop :

        def __init__(self):

            self.model = "hp"
            self.ram   = 8

        def show(self):

            print(self.model,self.ram)



s = Student("Ruchir",22)
s.show()