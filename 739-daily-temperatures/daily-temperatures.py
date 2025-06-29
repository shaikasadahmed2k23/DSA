class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = []
        s = []
        n = len(t)
        for i in range(n-1,-1,-1):
            while s:
                if t[i] >= t[s[-1]]:
                    s.pop()
                else:
                    break
            if s:
                c = s[-1] - i
                res.append(c)
            else:
                res.append(0)
            s.append(i)
        return res[::-1]