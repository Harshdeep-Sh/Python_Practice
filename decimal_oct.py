n=int(input("ENTER NUMBER: "))
lst=[]
rem=0
deci=n
while deci>0:
    rem=deci%8
    lst.append(rem)
    deci=deci//8

lst.reverse()

for i in lst:
    print(i,end="")






























'''
n=int(input("ENTER NUMBER: "))
quo=n//8

x=0
while quo>=8:
    quo=quo//8
    x+=1


print("quo=n//8=",quo)
rem=n%8
print("rem=n%8=",rem)
oc=(10*quo*(10**x))+rem
print(oc)
print(oct(n))'''