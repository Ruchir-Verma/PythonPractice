'''
Lists are use to store multiple values , either heterogenous  or homogenous.

'''

x = [1,2,'ruchir']
print(x)

print(x[0])

print(x[-1])  #supports negative indexing

'''
Lists are mutable , that is , we can replace an index ith different values.
'''

x[0] = 5
print(x)

'''
We can have lists or lists 
'''

x = [1,2,3]
y=['a','b','c']

z = [x,y]
print(z)

print(z[0][2])

'''
Operations in Lists :


'''

x = [1,2,3]
x.append(5)
print('After append ' ,x)

y=x.copy()
print('After copy function' ,y)

x.extend(y)
print('After extend x with y',x)

x.clear()
print('Afetr clearing x',x)

x = [1,7,9,4,2,3]
x.reverse()
print('After reversing x',x)

x.insert(0,'ruchir')
print('Ater adding any value into a particular position' ,x)

x.remove('ruchir')
print('After removng value 9 from list' , x)

x.sort()
print('After sorting',x)

x.pop()
print('Removes last element from a list',x)

x.pop(3)
print('Removing element of index 3',x)

del x[2:]
print('Deletes everything after position 2 ',x)


'''
We can find min,max,average,sum etc of a list
'''

x = [12,3,4,5,6,3]
print(max(x))

print(min(x))

print(sum(x))

print(sum(x)//len(x))