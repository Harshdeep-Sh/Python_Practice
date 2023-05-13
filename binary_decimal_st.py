n=int(input("ENTER NUMBER: "))
st=str(n)
num=0
p=0
rst=st[::-1]
for i in rst:
    num+=int(i)*(2**p)
    p+=1
print(num)
    


