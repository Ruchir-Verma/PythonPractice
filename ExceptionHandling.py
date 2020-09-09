'''
We have three types of errors:

1.Compile-time error  : syntax errors
2.Logical error      :  code gives output , but not a correct output
3.Runtime error      : code gets compiled , gives a correct output ,but sometimes it could  not perform certain operation(division by zero)

The moment we get runtime error , our execution stops.
To avoid this,we use exception handling

'''


a=5
b=0

try:
    print("resource open")
    c=a/b   #exception here,jumping to exception
    print(c)

except Exception as e:   #e not necessary
    print("Cannot divide by zero",e)

finally:
    print("resource close")




print("Bye")


'''
Types of exception :

1.zero division error
2. value error (e.g. when we define input as int ,but taking input as string)



'''

