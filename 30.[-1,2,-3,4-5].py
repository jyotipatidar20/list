list =[-1,2,-3,4,-5,6,-7,8,-9]
i=0
b=[]
while i<len(list):
    if list[i]<0:
        b.append(list[-i]*0)
    else:
        b.append(list[i])
    i=i+1
print(b)



