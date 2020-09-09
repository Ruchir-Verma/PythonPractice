'''
Functions are the sets of instructions that performs a certain task.It promotes code reusability.

We define function using degf statement.

'''


def add(x,y):
    c = x+y
    print(c)

add(5,6)


'''
A function can return a value as well
'''

def add(x,y):
    c = x+y
    return c

sum = add(5,6)
print(sum)

'''
We can return multiple values as well
'''

def add_sub(x,y):

    add = x+y
    sub = x-y
    return add,sub

a,b = add_sub(6,5)
print(a,b)
