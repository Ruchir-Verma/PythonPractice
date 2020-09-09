'''
Two types:

1.Instance Variables : They can be different for different objects
2.Class Variables  : They are same for every objects.If changed , it will affect the values in all the objects

'''

'''
namespace is an area where we we create and store object/variable.

types:

    class namespace,
    instance namespace.

'''

class Car :

    wheels = 4  #Class Variable

    def __init__(self,color,model):
        self.colour = color                #instance variables
        self.model = model

car1 = Car('red','BMW')
car2 = Car('blue' , 'Audi')

print(car1.colour,car1.model,Car.wheels)
print(car2.colour,car2.model,car2.wheels)