'''

Entry controlled loop

'''

''' Q . Program to print 'Ruchir Verma Verma Verma'  four times '''


i = 1

while(i<=4):
    print('Ruchir ',end="")
    j=1
    while(j<=3):
        print('Verma ',end="")    # end="" is used to avoid going to newline, since print always goes to new line after printing.
        j=j+1
    i=i+1
    print()