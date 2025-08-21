class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        num = sum(int(digit) for digit in str(num))
        return self.addDigits(num)
