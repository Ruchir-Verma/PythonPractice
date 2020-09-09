'''
Classes are the blueprints ,objects are the instance of a class

'''


class Employee:

    def details(self):

        print("Ruchir , 23, 1997")



'''
employee = Employee()
Employee.details(employee)   #self act as an argument which points to object
'''

employee = Employee()   #creates object

employee.details()