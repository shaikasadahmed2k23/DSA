class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mx = 0
        f = {}
        for i in arr:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        for i in f:
            if f[i] == i:
                if i>mx:
                    mx = i
        if mx != 0:
            return mx
        return -1
