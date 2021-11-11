elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
length=len(elements)
sum=0
even=0
odd=0
for i in elements:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print(even,"total even")
print(odd,"total odd")
print(len(elements),"total of elements")
even_count=0
odd_count=0
for i in elements:
    if i%2==0:
        even_count=even_count+i
    else:
        odd_count=odd_count+i
print(even_count,"total sum  of even") 
print(odd_count,"total  sum of odd")
i=0
sum=0 
while i<len(elements):
    sum=sum+elements[i]
    a=sum/len(elements)
    i=i+1
print(sum,"sum of all elements")
print(a,"average of all elements")
i=0
c=0
d=0
k=[]
y=[]
sum=0
sum1=0
while i<len(elements):
    b=elements[i]
    if b%2==0:
        k.append(b)
        sum=sum+b
        c=sum/len(k)
    else:
        y.append(b)
        sum1=sum1+b
        d=sum1/len(y)
    i=i+1
print(c,"even average")
print(d,"odd average")

