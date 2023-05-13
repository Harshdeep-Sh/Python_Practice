R0=int(input("ENTER RANGE: "))
R1=int(input("ENTER NUMBER: "))
r=[R0,R1]

def factor_form(r,n):
    quo=r//n
    rem=r%n
    print(r,"=",quo,"*",n,"+",rem)
    return n,rem


x,y=factor_form(r[0],r[1])
r.append(x)
r.append(y)
i=2
while y>1: 
    x,y=factor_form(r[i],r[i+1])
    r.append(x)
    r.append(y)
    i=i+2
print(r)
def inverse(r0,r1):
    
    for i in range(1,r0):
        if (r1*i)%r0==1:
            inv=i
            break
    return inv    

if y!=1:
    print("INVERSE DOES NOT EXIST! ")

if y==1:
    print("INVERSE IS: ",inverse(r[0],r[1]))
    