'''

Tuples are like lists , but it is immutable .

'''

x = (1,2,3)
print(x)

print(x[0])

#x[0] = 5   it will show error as tuple is immutable

print(len(x))

'''
Iteration in tuple is faster than list

'''


##################################################


''' Sets are the data types that returns only unique values and each time we run , we can different sequence
while printing.That is why indexing is not supported'''

s={1,2,4,1,2,3,1}
print(s)