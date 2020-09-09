'''
__init__ is a method that is used as a constructor ,or to initialise any object.

Whenever a constructor is there in a class, during the object creation , that constructor method is called by default.

'''


class Employee:

    def __init__(self):   #self is an argument that points to object

        print("This is a constructor")


    def details(self):

            print("Ruchir ,23 , 1997")


employee = Employee()
employee.details()


#############################################

class Student :

    def __init__(self,name,age):

        self.name = name
        self.age = age

    def details(self):

        print(self.name,self.age)


student = Student('Ruchir',22)
student.details()


#########  COMPARING THE OBJECTS  #########


class Details :

    def __init__(self,name,age):

        self.name = name
        self.age = age

    def details(self):

        print(self.name,self.age)


    def compare(self,object):

        if(self.age==object.age):
            print("Equal")
        else:
            print("Unequal")


student1 = Details('Ruchir',22)
student2 = Details('Tanuj',23)

student1.compare(student2)

