a=[1,2,"j","y","o","t","i",7,8,"s","a","p","n","a",7,3,"u","e"]
print(a)
i=0
b=[]
while i<len(a):
    if type(a[i])==str:
            b.append(a[i]) 
    i=i+1
print(b)
j=0
c=[]
while j<len(a):
    if a[j]=="a" or a[j]=="e" or a[j]=="i" or a[j]=="o" or a[j]=="u":
        c.append(a[j])
    j=j+1
print(c)


