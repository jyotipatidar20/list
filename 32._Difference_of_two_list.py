list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
# length=len(list1)
# length=len(list2)
i=0
a=[]
for i in list1:
    if i not in list2:
        a.append(i)
print(a)
