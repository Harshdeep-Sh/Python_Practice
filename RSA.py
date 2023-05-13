
x=int(input("ENTER MESSAGE(plain text): "))

#For B
p=3
q=11
phi=(p-1)*(q-1)

e=3
for i in range(1,phi):
    if (e*i)%phi==1:
        d=i
        break


print("Kpub = (",phi,",",e,") is sent to A")

#Encryption
y=(x**e)%phi

print("Cipher Text y=",y," is sent to B")

#Decryption
p=(y**d)%phi

print("Decrypted Plain Text= ",p)
