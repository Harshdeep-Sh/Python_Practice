# ones = 0 >> +0
# ones = 1 >> 0 + right + 1
# ones >=2 >> 0*ones + 1

# tens = 0 >> 0
# tens = 1 >> 1 + right + 1
# tens >=2 >> 1*tens + 10

# hund = 0 >> 0
# hund = 1 >> 20 + right + 1
# hund >=2 >> 20*hund + 100

# thou = 0 >> 0
# thou = 1 >> 300 + right + 1
# thou >=2 >> 300*thou + 1000

# tth = 0 >> 0
# tth = 1 >> 4000 + right + 1
# tth >=2 >> 4000*tth + 10000

# general pattern
# dig = 0 >> 0
# dig = 1 >> mul*(10^(p-1)) + right + 1
# dig >=2 >> mul*(10^(p-1))*int(dig) + (10^p)

n = int(input())
sn = str(n)
count = 0
l = len(sn)
for i in range(0, l):
    if (int(sn[l-i-1]) == 1):
        count += i*(10**(i-1)) + n%(10**(i)) + 1

    if (int(sn[l-i-1]) >= 2):
        count += i*(10**(i-1))*int(sn[l-i-1]) + (10**i)

print(int(count))


# def countDigitOne(n):
#     countr = 0
#     i = 1
#     while (i <= n):
#         divider = i * 10
#         countr += (int(n / divider) * i + min(max(n % divider - i + 1, 0), i))              
#         i *= 10

#     return countr


# # Driver Code
# print(countDigitOne(n))
