p=input("ENTER MESSAGE: ")
key=input("ENTER KEY: ")
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
kl=[]
for i in range(len(key)):
    kl.append(key[i])

def key_generator(k):
    m=len(p)//len(k)
    a=len(p)-m*len(k)
    ekey=k*m
    rem=''
    for i in range(a):
        rem+=kl[i]
    ekey=ekey+rem
    return ekey

Exkey=key_generator(key)
ekl=[]    
for i in range(len(Exkey)):
    ekl.append(Exkey[i])


pl=[]
for i in range(len(p)):
    pl.append(p[i])    


posl=[]
cl=[]
for i in range(len(p)):
    c=l.index(pl[i]) + l.index(ekl[i])
    posl.append(c)
    pos=c%26
    ele=l[pos]
    cl.append(ele)
    

print("ENCRYPTED MESSAGE: ")
for i in range(len(p)):
    print(cl[i],end="")
    
print()
de=''

for i in range(len(p)):
    q=(posl[i] - l.index(ekl[i]))
    de+=l[q%26]
    
print("DECRYPTED MESSAGE: ")
print(de)









