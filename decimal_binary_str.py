n=int(input("ENTER NUMBER: "))
st=""
rem=0
deci=n
while deci>0:
    rem=deci%2
    r=str(rem)
    st+=r
    deci=deci//2

rst=st[::-1]


for i in rst:
    print(i,end="")