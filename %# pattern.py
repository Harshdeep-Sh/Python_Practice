def pattern(n):
    for i in range(n,0,-1):
        if i%2==0:
            print("% "*i)
        else:
            print("# "*i)
n=int(input("ENTER NUMBER OF PATTERNS "))
pattern(n)

