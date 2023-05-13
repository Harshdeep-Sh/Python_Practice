n=int(input("ENTER NUMBER OF PATTERNS "))

print(" "*n+"*")
for i in range(1,n+1):
    print(" "*(n-i)+"*"*2*i)



for i in range(n,0,-1):
    print(" "*(n-i)+"*"*2*i)
print(" "*n+"*")