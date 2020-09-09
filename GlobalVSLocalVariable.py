a = 15

def show():
    a=10
    print('Local',a)

show()           #Local variable. Function always give preference to a local variable
print('Global',a)


'''
If we want to point out the same global variable in that function , we need to explicitly define with globl keyword
'''

a=15
def view():
    global a
    a=10
    print("Local" ,a )

view()
print('Global',a)


'''
If we want to change the global variable value inside a function ,without affecting the local variable value
'''


b = 9

def show2():

    b = 10
    print('Local : ',b)

    globals()['b'] = 19

show2()
print('Global changed : ',b)
