numbers = [1,2,3,4,5,6,7,8]
max=numbers[0]
min=numbers[0]
j=0
sum=0
pro=1
for i in numbers:
    if i > max:
        max=i
    if i<min:
        min=i
while j<len(numbers):
    pro=pro*numbers[j]
    sum=sum+numbers[j]
    avg=sum/numbers[j]
    j=j+1
print("maximum number is ", max)
print("minimum number is",min)
print(pro)
print(sum)
print(avg)
    
