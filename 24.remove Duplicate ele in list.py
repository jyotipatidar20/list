list=[1,3,2,3,1,6,6,4,3,21]
remove_duplicates=(list)
a = []
for x in list:
        if x not in a:
            a.append(x)
print(a)