

def sort(list):

    for i in range(5):
        minpos = i
        for j in range(i,6):
            if(list[minpos]>list[j]):
                minpos = j

        temp = list[i]
        list[i]=list[minpos]
        list[minpos]=temp

    return list









l = [4,9,0,1,7,3]
x = sort(l)

print(x)
