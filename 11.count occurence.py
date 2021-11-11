a = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
l=[]
while i<len(a):
    j=0
    b=[]
    count=0
    while j<len(a):
        if a[i]==a[j]:
            count=count+1
        j=j+1
    b.append(a[i])
    b.append(count)
    if b not in l:
        l.append(b)
    i=i+1
print(l)

