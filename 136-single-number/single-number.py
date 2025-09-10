class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # f = {}
        # for i in nums:
        #     if i in f:
        #         f[i] += 1
        #     else:
        #         f[i] = 1
        # for i in f:
        #     if f[i] == 1:
        #         return i
        x = 0
        for i in nums:
            x ^= i
        return x