'''
Python does not supports pass by value or pass by reference

'''


'''
Types of arguments

1.Formal Arguments
2.Actual Arguments ---> They are of 4 types : 
                                  1. Position
                                  2. Default
                                  3. Keyword
                                  4. Variable Length
'''


def add(x,y):   #Formal Argument
    return x+y



add(4,5)      #Actual Argument


'''
Keyword Arguments
'''

def details(name,age):
    print(name)
    print(age)

details(name = 'Ruchir', age = 25)


'''
Default Arguments
'''

def details(name,age=18):
    print(name)
    print(age)

details(name='Ruchir')       #age can be overide here



'''
Variable length arguments
'''

def addition(a,*b):    #b becomes tuple thatvv will store all the elements after the first element

    sum = a
    for i in b:
        sum=sum+i

    return sum


print(addition(12,5))
print(addition(1,2,3,4))



'''
Keyworded Variable length arguments
'''

def data(name , **details):
    print(name)
    print(details)

data('Ruchir' , age = 28 , City = 'Bangalore' , mob = 9876543)



