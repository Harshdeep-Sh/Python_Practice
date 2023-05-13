def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    if n>2:
        return (fibo(n-1) + fibo(n-2))
    
n=int (input("ENTER NUMBER OF TERMS "))
if n<0:
    print("PLEASE ENTER A POSITIVE NUMBER")
else:
    for i in range(1,n+1):
        print(fibo(i),end="  ")
    
