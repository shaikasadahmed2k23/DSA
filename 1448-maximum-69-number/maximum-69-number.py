class Solution:
    def maximum69Number (self, num: int) -> int:
        s1 = list(str(num))
        for i in range(len(s1)):
            if s1[i] == '6':
                s1[i] = '9'
                break 
        return int(''.join(s1))
