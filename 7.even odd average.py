elements = [23, 14, 56, 12, 19, 9, 15, 25, 31,42,43]
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
print("even average",c)
print("odd average",d)
        

























# even_count=0
# odd_count=0
# i=0
# sum=0
# sum2=0
# c=[]
# y=[]
# while i<len(elements):
#       a=elements[i]
#       if a%2==0:
#           c.append(a)
#           sum=sum+a
#           even_count=sum/len(c)
#       else:
#           y.append(a)
#           sum2=sum2+a
#           odd_count=sum2/len(y)
#       i=i+1
# print("even average",c)
# print("odd average",y)

















