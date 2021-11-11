b=[1,2,3,[4,5],6,[8,9,2]]
i=0
a=[]
while i<len(b):
    if type(b[i])==list:
        j=0
        while j<len(b[i]):
            a.append(b[i][j])
            j=j+1
    else:
        a.append(b[i])
    i=i+1
print(a)
    
