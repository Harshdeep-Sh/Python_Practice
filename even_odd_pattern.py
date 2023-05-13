def patt(n):
    for i in range(n):
        x=2
        y=1
        for j in range(n-i,0,-1):
            if i%2==0:
                print(y,end=" ")
                y+=2
            if i%2==1:
                print(x,end=" ")
                x+=2
        print()
n=int(input("ENTER NUMBER OF ROWS "))
patt(n)



def patt1(n):
    c=0
    for i in range(n,1,-1):
       
        if i%2==1:
            for j in range(2*(n)-c):
                if j%2==1:
                    print(j,end=' ')
            print() 
              
        if i%2==0:
            for j in range(1,2*(n)-c):
                if j%2==0:
                    print(j,end=' ')
            print()
        c+=1
                
