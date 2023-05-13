import math
n = int(input())
counter = 0

counter+=math.floor(n/100)
n=n%100
counter+=math.floor(n/50)
n=n%50
counter+=math.floor(n/20)
n=n%20
counter+=math.floor(n/10)
n=n%10
counter+=math.floor(n/5)
n=n%5
counter+=math.floor(n/2)
n=n%2
counter+=n
print(counter)
