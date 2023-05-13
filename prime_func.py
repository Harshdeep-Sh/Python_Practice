n=int(input("ENTER THE NUMBER "))

def prime(x):
    pr="prime"
    for i in range(2,x):
        if (x%i)==0:
            factor=i
            pr="not prime"
            break
    if pr=="prime":
        print("NUMBER IS PRIME")
    else:
        print("NUMBER IS NOT PRIME")
        print(factor,"times",x//factor,"is",x)
        
prime(n)