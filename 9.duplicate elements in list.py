list=[0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5,9]
i=0
while i<len(list):
    j=i+1
    while j<len(list):
        if list[i]==list[j]:
            del(list[j])
        else:
            j=j+1
    i=i+1
print(list)







                                                                                                                                                                                 