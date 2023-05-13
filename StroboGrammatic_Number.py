n = int(input("Enter Number "));
Num = n 
New_num = 0
flag= 1
while(n>0 and flag == 1):
    rem = n%10
    n = n//10
    if(rem==1 or rem==8 or rem==0):
        New_num = New_num*10 + rem
    elif(rem==9):
        New_num = New_num*10 + 6
    elif(rem==6):
        New_num = New_num*10 + 9
    else:
        flag = 0
if(Num==New_num):
    print("Yes")
else:
    print("No")