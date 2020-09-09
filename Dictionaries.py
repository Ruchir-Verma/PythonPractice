'''

Dictionaries are key valye pairs, in which key are immutable

'''

dic ={
    1:'ruchir',
    2:'shubham',
    3:'karan',
    4:'tanuj',
}

print(dic[4])  # returns Tanuj

dic[4] = 'Ayush'  #overrides Tanuj with Ayush

print(dic)


print(dic.items())


'''
Suppose we have to give some default values to the keys ,which are not present in dictionay. Then use get() method
'''

print(dic.get(1))



print(dic.get(5,'Not found'))

'''
Suppose we want to make a make a dictionary keys and values using two lists , we can use zip function.
'''

x = ['Ruchir', 'Tanuj' , 'Ritik']
y = ['Python' , 'Java' , 'JS']


list = dict(zip(x,y))
print(list)


'''
We can append key value in the dictionary 
'''

list['Shubham'] = 'Angular'
print(list)


'''
If we want to delete a kev value pair,use del function
'''

del list['Shubham']
print(list)

'''
We can store lists and dictionaries as values in dictionaries 

'''

dic = {'Java' : ['Eclipse','Spring'] ,'JS' : 'Atom' , 'Python' : { 'Python 2.7' : 'Pycharm', 'Python 3.7': 'ML'}}

print(dic)

print(dic['Java'])
print(dic['Python'])

'''
Use dic.keys() to get all keys and dic.values() to get all the values in a dictionary.
'''