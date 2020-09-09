'''
Using decorators we can add some extra features in our function

'''

#Example:

def div(a,b):
    return a/b


'''
div(2,4) will return 0.5 

But if we want a condition such that always larger number should be taken as numerator as smaller number as denominator
without affecting the function definition,we can use the concept of decorators.
'''


def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b=b,a

        return func(a,b)
    return inner


x = smart_div(div)
print(x(2,4))