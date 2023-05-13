def prime(x):
    pr="prime"
    for i in range(2,x):
        if (x%i)==0:
            pr="not prime"
            break
    if pr=="prime":
        return ("y")
    else:
        return("n")
    
n=int(input("ENTER THE NUMBER: "))
lst=[]
for i in range(1,(n+1)):
    div=n%i
    if div==0 and prime(i)=="y":
        lst.append(i)
        
print("PRIME FACTORS OF",n,"ARE ")
for i in lst:
    print(i)
        
        
