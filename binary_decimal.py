def itl(n):
    lst=[]
    while n>0:
        rem=n%10
        lst.append(rem)
        n=n//10
    return lst
n=int(input("ENTER NUMBER: "))
lst=itl(n)
num=0
lst.reverse()
for i in range (len(lst)):
    num+=lst[i]*(2**i)
print(num)
   








