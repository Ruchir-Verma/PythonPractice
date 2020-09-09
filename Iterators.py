'''
Iterators are used to traverse or iterate over any object.


We can use next function to get the nnexrt immediate value . It preserves the state of previous value and give us the
next immediate value everytime we calls it

'''

l = [1,2,3,4,5]

it = iter(l)
print(it.__next__())
print(it.__next__())


'''
USER DEFINED ITERATOR


for achieving this we need to define two methods , iter() and next()


'''


#define an iterator


class Iterator:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        val = self.num
        self.num+=1
        return val

i = Iterator()
print(i.__next__())


#
#define an iterator  which orints first 10 values


class Iterator:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if(self.num<=10):
         val = self.num
         self.num += 1
         return val
        else:
            raise StopIteration

i1 = Iterator()

for i in i1:     #for loops internally calls __next__ function
    print (i)