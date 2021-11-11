magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
v=15
while i<len(magic_square):
    row=0
    c=0 
    sum=0
    while row<len(magic_square[i]):
            c=c+(magic_square[i][row])
            row=row+1
    sum=sum+c
    i=i+1 
print(sum,"rows")
j=0
while j<len(magic_square):
    col=0
    k=0
    sum1=0
    while col<len(magic_square[j]):
        k=k+(magic_square[j][col])
        col=col+1
    sum1=sum1+k
    j=j+1
print(sum1,"columns")
x=magic_square[0][0]+magic_square[1][1]+magic_square[2][2]
y=magic_square[0][2]+magic_square[1][1]+magic_square[2][0]
if x==v :
    if y==v:
        d=x+y
        print(d,"diagonal")
        if sum==sum1==x==y:
            print("it is a magic square")
        else:
            print("not a magic square")
    else: 
        print("it is not magic square")
else:
    print("it is not magic square")



