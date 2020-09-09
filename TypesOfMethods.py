'''
Theree types of methods :

1.  Class methods
2.  Statis methods
3. Instance methods


'''


class Student :

    school = "DPS"

    def __init__(self,m1,m2,m3):

        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


    def avg(self):                   #This is an instance method,work with instance variables

        return((self.m1+self.m2+self.m3)/3)

    @classmethod                     #This is a class methods , work with class variables
    def details(cls):

        return cls.school

    def info():                     #This is a static method,nothing do to with object or class variables

        return "This is Student  details class..."

s1 = Student(12,15,20)
s2 = Student(20,40,10)

print(s1.avg())
print(s2.avg())
print(Student.details())

'''
Instance methods have two types :

1.Accessors : When we just want to fetch the values


example :

         def getM1(self) : 
                   return self.m1
                   
                   
                   
         def  setM1(self,value)  :
                   return self.m1 = value       
2.Mutators

'''