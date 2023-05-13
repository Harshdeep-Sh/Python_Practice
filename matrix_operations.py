n=int(input("Enter size of matrix: "))
m1=[]
print("Matrix 1")
for i in range(n):
    ele=[]
    for j in range(n):
        ele.append(int(input()))
    m1.append(ele)

m2=[]
print("Matrix 2")
for i in range(n):
    ele=[]
    for j in range(n):
        ele.append(int(input()))
    m2.append(ele)

add=[]
for i in range(n):
    ele=[]
    for j in range(n):
        ele.append(m1[i][j] + m2[i][j])
    add.append(ele)

mul=[]
t = []
for i in range(n):
    ele=[]
    for j in range(n):
        ele.append(m2[j][i])
    t.append(ele)

for i in range(n):
    ele=[]
    for j in range(n):
        s=0
        for k in range(n):
            s+=m1[i][k]* m2[k][j]
        ele.append(s)
    mul.append(ele)

print("Matrix 1: ",m1)
print("Matrix 2: ",m2)
print("Sum: ",add)
print("Transpose: ",t)
print("Multiplication: ",mul)
    
