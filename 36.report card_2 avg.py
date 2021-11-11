marks = [
     [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
i=0
count=0
while i<len(marks):
    j=0
    sum=0
    c=0
    while j<len(marks[i]):
        c=c+(marks[i][j])
        j=j+1
    sum=sum+c
    avg=sum//len(marks[i])
    i=i+1
    count=count+1
    print( avg,"avg of" ,count ,"year ")




# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65] ,  
#     [95, 45, 78]
# ]
# i=0
# count=0
# while i<len(marks):
#     j=0
#     c=0
#     sum=0
#     while j<len(marks[i]):
#         c=c+(marks[i][j])
#         j=j+1
#     sum=sum+c
#     avg=sum//len(marks[i])
    # i=i+1
    # count=count+1
    # print(avg,"avg of",count,"year")


# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78],
#     [87, 67, 49, 68, 88]
# ]
# i=0
# count=0
# while i<len(marks):
#     j=0
#     c=0
#     sum=0
#     while j<len(marks[i]):
#         c=c+(marks[i][j])
#         j=j+1
#     sum=sum+c
#     avg=sum//len(marks[i])
#     i=i+1
#     count=count+1
#     print(avg,"avg of ",count,"year")