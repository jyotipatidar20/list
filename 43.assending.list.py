s=[1,2,8,7,6,3,4,8,9,5,10]
i=0
b=[]
for i in range(len(s)):
    if s[i]%2==0:
        pass
    else:
        b.append(s[i])
print(b)       
i=0
for i in range(len(b)):
    j=i
    temp=0
    for j in range(len(b)):
        if b[j]>b[i]:
            temp=b[i]
            b[i]=b[j]
            b[j]=temp
i=0
for i in range(len(s)):
    if s[i]%2==0:
        a=s.index(s[i])
        b.insert(a,s[i])
print(b)