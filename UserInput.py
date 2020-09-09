'''

To get the input from the user , we have to use input() function .

'''

x = input('Enter 1st number')
y = input('Enter 2nd Number')

z = x+y

print(z)  # It will print xy(in the form of string)


'''
To get the sum , we have to provide the data type with input function as follows :
'''

x = int(input('Enter 1st number'))
y = int(input('Enter 2nd number'))

z = x+y

print(z)


'''
We can use 'eval' function to get the result during the time of input
'''

x = eval(input('Enter expression'))
print(x)

'''
To get the input from the command line, use argv function 

'''

import sys
x = int(sys.argv[1])
y=int(sys.argv[2])

z = x+y
print(z)