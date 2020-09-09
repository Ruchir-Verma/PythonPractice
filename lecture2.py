# opertors

#Point to remember :
'''

1 . Division always returns floating value. If we want to get only the integer or quotient value , we need to do floor
division.


E.g  4/2 = 2.0
    4//2 = 2    (floor division)

'''

x=4/2
print(x)

y=4//2
print(y)

'''
2 .To perform 'to the power' operations, use **.
  
'''

x = 2**3
print(x)

'''
3 .To get remainder values : use %
'''

x = 10%3
print(x)


'''
4 .When printing a string , it will give syntax error if we use like this  :

print(  ' ruchir's laptop ' ) 

To ignore this kind of scenario , use \  as following :


'''
print( ' ruchir\'s laptop')


'''
5 . Suppose we want to print as :

print('C:\ruchir\newFolder')

output :  C:/ruchir
        ewFolder 
As python is taking \n as new line . To get the string as it is in such scenarios , use raw command (r).
'''

print(r'C:\ruchir\newFolder')



