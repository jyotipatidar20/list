v=[9,6,5,4,8,1,2,7,3,0]
# i=0
for j in range(0,10):
    for i in range(0,9):
        if v[i]>v[i+1]:
            b=v[i]
            v[i]=v[i+1]
            v[i+1]=b
        # i=i+1
    # j=j+1
print(v)



