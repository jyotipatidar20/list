list=[1,"bhumika",2,"kittu",3,"jiyanshi",4,"aastha",5,"sapna",6,"jyoti",7,"saloni",8,"sheetal"]
print(list)
i=0
n=[]
while i < len(list):
    if type(list[i])==str:
        n.append(list[i])
    i=i+1
print(n)






