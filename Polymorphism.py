'''
In programming, polymorphism means same thing but different forms.

4 ways to implement polymorphism in python

1. Duck Typing
2. Operator Overloading
3. Method Overloading
4. Method Overriding

'''

'''
Duck Typing
'''

class PyCharm :

    def execute(self):

        print("Compile")
        print("Running")

class Atom :


    def execute(self):
        print("Compile")
        print("Running")


class Laptop:

    def code(self,ide):          #ide can be a object of any class, if that class has execute method , it will run.
                                #This is called as duck typing.
        ide.execute()



x = Atom() #or x=PyCharm()
y = Laptop()

y.code(x)


