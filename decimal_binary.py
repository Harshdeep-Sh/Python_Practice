n=int(input("ENTER NUMBER: "))
lst=[]
rem=0
while n>0:
    rem=n%2
    lst.append(rem)
    n=n//2
lst.reverse()
for i in lst:
    print(i,end="")