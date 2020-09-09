pos = 0

def search(list,n):

    for i in list:
        if(i==n):
            global pos
            pos=i
            return True
    return False




list = [1,2,3,4,5,6]
n=3

if search(list,n):
    print("Found at ",pos)

else :
    print("Not Found")