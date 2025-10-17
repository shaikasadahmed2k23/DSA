class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f = {}
        m = 0
        for i in nums:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
            m = max(m,f[i])
        c = 0
        for k,v in f.items():
            if v == m:
                c += v
        return c