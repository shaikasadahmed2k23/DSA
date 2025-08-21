class Solution:
    def addDigits(self, num: int) -> int:
        # Base case: If num is a single digit, return it
        if num < 10:
            return num
        
        # Recursive case: Sum the digits and call the function again
        num = sum(int(digit) for digit in str(num))
        
        # Recursively call addDigits with the sum of digits
        return self.addDigits(num)
