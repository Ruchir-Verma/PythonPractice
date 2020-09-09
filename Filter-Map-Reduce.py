
'''

FILTER
'''
is_even = lambda a:a%2==0
num=[1,2,3,4,5,6,7,8,9,10]
evens= list(filter(is_even,num))
print(evens)

'''
MAP
'''

doubles = list(map(lambda a:a+2,evens))
print(doubles)


'''
REDUCE

we need to import functools module for it
'''
from functools import reduce
sum = reduce(lambda a,b : a+b ,doubles)
print(sum)
