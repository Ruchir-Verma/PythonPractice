'''
for binary searcch, all values should be sorted


'''

l = [10,14,12,19,1,6,9,0,3]

pos = 0

def search(list,n):

    l = 0
    u =len(list)-1
    mid=(l+u)//2

    while(l<u):
       if(n>list[mid]):
          l=mid

       elif(n<list[mid]):
          u=mid

       else:
           mid = (l+u)//2
           if(list[mid]==n):
               return True

       return False





l.sort()

if(search(l,99)):

    print("Found")

else:

    print("Not Found")

