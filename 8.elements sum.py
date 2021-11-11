elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
even_count=0
odd_count=0
while i<len(elements):
    sum=sum+elements[i]
    if i%2==0:
        even_count=even_count+i
        a=sum/len(elements)
    else:
        odd_count=odd_count+i
        b=sum/len(elements)
    i=i+1
print(sum)
print("even_count",a)
print("odd_count",b)

