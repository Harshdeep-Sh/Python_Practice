class Solution:
    def countDigitOne(self, n: int) -> int:
        sn = str(n)
        count = 0
        l = len(sn)
        for i in range(0, l):
            if (int(sn[l-i-1]) == 1):
                count += i*(10**(i-1)) + n%(10**(i)) + 1

            if (int(sn[l-i-1]) >= 2):
                count += i*(10**(i-1))*int(sn[l-i-1]) + (10**i)

        return(int(count))
