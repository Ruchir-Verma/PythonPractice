'''
Data Types in Python :

1.None -- > when variables are not assigned with values.
2.Numeric -- > int,float,complex,bool

<------sequence------->
3.List
4.Tuple
5.Set
6.String
7.Range
<---------------------->
8.Dictionary

'''

x=2j
print(type(x))

# conversion between data types
a=5.6
b=int(a)
print(b)
b=float(b)
print(b)

#To create a complex number,use complex function

a=5
b=6
c=complex(a,b)
print(c)


'''
There is no char type in string . We only have string data type in Python
'''

x = 'r'
print(type(x))
################################
print(range(10))
x=list(range(10))
print(x)

'''
To print table of 2 using range
'''

x = list(range(2,22,2))
print(x)