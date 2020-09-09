def sort(list):

    for i in range(len(list)-1):
        for j in range(0,len(list)-1-i):
            if(list[j]>list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

    return list


l = [4,9,0,1,7,3]
print(sort(l))




