tot = int(input())
c=0
for i in range(1,tot//2 + 1):
    for j in range(1,tot//4 + 1):
        if(i*2 + j*4 == tot):
            print(i,j)
            c+=1
print("count=",c)
