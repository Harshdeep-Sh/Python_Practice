p=29
a=2

KprA=int(input("ENTER PRIVATE KEY FOR A: "))
KprB=int(input("ENTER PRIVATE KEY FOR B: "))

#Public Key
KpubA=(a**KprA)%p
KpubB=(a**KprB)%p

print("PUBLIC KEYS KpubA= ",KpubA,"and KpubB= ",KpubB,"are shared")

#Common Secret Key

Kab=(KpubB**KprA)%p
Kba=(KpubA**KprB)%p

print("AFTER KEY EXCHANGE, Kab= ",Kab,"and Kba= ",Kba)