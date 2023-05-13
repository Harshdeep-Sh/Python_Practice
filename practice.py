'''a=input("enter string 1")
b=input("enter string 2")
c=input("enter string 3")
f=a+b+c
l=len(f)
print(l)
for i in range(2,l):
    ip=1
    if l%i==0:
        ip=0
        break
if ip==1:
    print("PRIME")
else:
    print("NOT PRIME")
    
a='2'
b='3'
j=1
for i in range(1,6):
    if i%2==1:
        print(a*j)
    else:
        print(b*j)
    j+=2


def f1(a,b,c):
    m=a*b*c
    return m

def f2(x):
    n1=0
    n2=1
    y=0
    if x>=2:
        print(n1)
        print(n2)
        for i in range(x):
            y=n1+n2
            n1,n2=n2,y
            if y>=x:
                break
            print(y)
    elif x==1:
        print(0)
    else:
        print("NONE")
        
a=int(input("ENTER "))
b=int(input("ENTER "))
c=int(input("ENTER "))
val=f1(a,b,c)
f2(val)   


a=int(input("ENTER "))
b=int(input("ENTER "))
v=int(input("ENTER "))
m=a*b*v
s=str(m)
su=0
for i in range(len(s)):
    x=int(s[i])
    
    su+=x**len(s)
    
if su==m:
    print("armstrong")
else:
    print("no")




for i in range(1,5):
    j=0
    while j<i:
        if j%2==1:
            print('0',end="")
        else:
            print('1',end="")
        j+=1
    print()




 
for x in range(1,5):
    y=0
    c=x
    while y<x:
        if c%2==0:
            print(0,end="")
            c+=1
        else:
            print(1,end="")
            c+=1
        y+=1
    print()
    
n=int(input("enter "))   
n1=0
n2=1
for i in range(1,n+1):
    if i==1:
        print(0)
    elif i==2:
        print(1)
    else:
        n1,n2=n2,n1+n2
        f=n2
        print(f)
    
        
a='%'
b='@'
j=1
for i in range(1,8):
    if i%2==1:
        print(a*j)
        j+=1
    else:
        print(b*j)
        j+=1
        
n=int(input("ENTER NUMBER "))
c=0
for i in range(2,n):
    if n%i==0:
        c+=1
if c==0:
    print('prime')
else:
    print("no")        

def f1(n,m):
    s=n+m
    return s
def f2(x):
    for i in range(x):
        if i%2==0 and i%3==0:
            print(i)
a=int(input("ENTER NUMBER "))
b=int(input("ENTER NUMBER "))
y=f1(a,b)
f2(y)

w=int(input("ENTER NUMBER "))
x=float(input("ENTER NUMBER "))
y=float(input("ENTER NUMBER "))
z=float(input("ENTER NUMBER "))
if w>x:
    a=w
else:
    a=x
if y>z:
    b=y
else:
    b=z
if a<b:
    print(a)
else:
    print(b)
    
a=int(input("num"))    
for i in range(a):
    for j in range(i+1):
        if i%2==0:
            print('%',end='')
        else:
            print('@',end='')
    print()
    
    
s=int(input("ENTER START NUMBER "))
l=int(input("ENTER END NUMBER "))
ln=0
for i in range(s,l):
    cn=i
    print(cn+ln)
    ln=cn
     
    
st=input("ENTER STRING ")
n=int(input("ENTER NUMBER "))
l=len(st)
ns=st[l-n:l]
print(ns)
     
        
def hm(n,l):
    s=0
    for i in l:
        s+=(1/i)
    
    hm=n/s
    return hm

n=int(input("ENTER NUMBER OF ELEMENTS "))
lst=[]
for i in range(n):
    x=int(input("ENTER ELEMENT "))
    lst.append(x)

print("HARMONIC MEAN IS",hm(n,lst))    
   
         
    
l=[1,1,0,1,1,1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1]

c=0
maxi=0
for i in range(len(l)):
    if l[i]==1:
        c+=1
        lon=c
    if l[i]==0:
        c=0
        lon=0
    if maxi<lon:
        maxi=lon
           
print(maxi)

  

        
    
    
    
n=int(input("ENTER THE NUMBER "))

def prime(x):
    pr=1
    for i in range(2,x):
        if (x%i)==0:
            pr=0
            break
    return pr
  
lsth=[]
for i in range(10,n+1):
    pri=prime(i)
    if pri==1:
        lsth.append(i)
                 
print(lsth)            
    
for i in range(2,100):
    if 131%i==0:
        print(i)

   
n=int(input("ENTER NUMBER "))
fact=1
if n==0 or n==1:
    fact=1
elif n>1:
    while n>1:
        fact*=n
        n-=1
else:
    print ("NEGATIVE VALUE!!!")        
    
    
print(fact)    
       

  
  

lst.sort()
print(lst)


d={}
for i in range(3):
    n=input("NAME ")
    m=int(input("MARKS "))
    d[n]=m
print(d)


sorted(d)



dict1 = {1: 1, 2: 9, 3: 4}
sorted_dict = {}
sorted_keys = sorted(dict1, key=dict1.get)  # [1, 3, 2]
print(sorted_keys)
for w in sorted_keys:
    sorted_dict[w] = dict1[w]

print(sorted_dict) # {1: 1, 3: 4, 2: 9}


n=int(input("ENTER NUMBER "))
m=int(input("ENTER NUMBER "))
i=m   
while i>1 :
    if n%i==0 and m%i==0:
        hcf=i
        break
    i-=1
print(hcf)



import array
lst=['a','f','c','d','a']
nlst=list(set(lst))
ar=array['i',nlst]
print(ar)



st='eed Dddd'
print(str.swapcase(st))

for i in range(1,2058):
    if 2057%i==0:
        print(i)
        
        

for i in range(1,187):
    if 187%i==0:
        print(i)
   '''
def search(list,n): 
    for i in range(len(list)): 
        if list[i] == n: 
            print('String found at index',i)
            break
    else:
        print('Not found')
arr = ['abc','def','ghi'] 
n = input('Enter string to search') 
search(arr,n)     







    
    
    
    
    
    
    
    
    
    
    