a=[1,2,[3,4],5,[6,7],8,9]
i=0
sum=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            j=j+1
    else:
        sum=sum+a[i]
    i=i+1
print(sum)



a=[[1,2,3],[1,2,3],[2,4,6]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a):
#      c=(a[i][j])
#      sum=sum+c
#      j=j+1
#     i=i+1
# print(sum)

i=0
sum=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            sum=sum+(a[i][j])
            j=j+1
    else:
        sum=sum+a[i]
    i=i+1
print(sum)