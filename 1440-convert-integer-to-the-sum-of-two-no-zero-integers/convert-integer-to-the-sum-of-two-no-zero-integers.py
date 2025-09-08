class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        res = []
        # for i in range
        # res.append(1)
        # res.append(n-1)
        # return res
        for i in range(n):
            x = n - i
            s1 = str(i)
            s2 = str(x)
            if '0' not in s1 and '0' not in s2:
                res.append(i)
                res.append(n-i)
                return res
