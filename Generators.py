'''
FIRST CHECK ITERATOR
'''

'''
Python provides Generator is a special function which can be used to implement the function of an iterator.
'''

def num():
    yield 5
    yield(4)              #multiple yields are allowed

x=num()
print(x.__next__())
print(x.__next__())



'''
PRINTING SQUARES USING GENERATOR
'''

def sq():

    x=1
    while(x<=10):
        a=x*x
        yield a   #return terminates the function,yield does not
        x=x+1



a=sq()
for i in a:
    print(i)