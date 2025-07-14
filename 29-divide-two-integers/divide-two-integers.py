class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        flag1 = flag2 = 0
        if dividend < 0:
            flag1 = 1
            dividend = abs(dividend)
        if divisor < 0:
            flag2 = 1
            divisor = abs(divisor)

        c = 0 
        while dividend >= divisor:
            temp = divisor
            ml = 1
            while dividend >= (temp << 1):
                temp <<= 1
                ml <<= 1
            dividend -= temp
            c += ml

        if flag1 != flag2:
            c = -c

        return max(min(c, 2**31 - 1), -2**31)
