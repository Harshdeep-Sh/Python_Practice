n=int(input("ENTER THE NUMBER: "))
lst=[]
for i in range(1,(n+1)):
    div=n%i
    if div==0 :
        lst.append(i)
        
print("FACTORS OF",n,"ARE ")
for i in lst:
    print(i)
        
        
