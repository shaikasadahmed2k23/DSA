class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            s = 0
            while n > 0:   # process ALL digits
                x = n % 10
                s += x ** 2
                n //= 10
            n = s  # update n with the new sum
        
        return n == 1
