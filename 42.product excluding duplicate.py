a=[1,2,1,2,3,4,3,4,5,6,5,6]
i=0
b=1
while i<len(a):
    j=i+1
    while j<len(a):
        if a[i]==a[j]:
            del(a[j])
            b=b*a[i]          
        else:
            j=j+1
    i=i+1
print(a)
print(b)