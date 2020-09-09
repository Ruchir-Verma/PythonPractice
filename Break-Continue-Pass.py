'''

Break is used to come out of a loop

'''

'''
continue is used to skip that particular iteration

'''

for i in range(1,10):
    if i%3==0:
        continue
    else:
        print(i,end=" ")


###########################################################


'''
pass is used when we just want to ignore some block , or when there is nothing to do with that particular condition
'''
print()
for i in range(1,10):
    if(i%2==0):
        pass
    else:
        print(i,end=" ")