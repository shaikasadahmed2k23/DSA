from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        s = []

        for i in range(2 * n - 1, -1, -1):
            while s and nums[i % n] >= s[-1]:
                s.pop()
            if s:
                res[i % n] = s[-1]
            s.append(nums[i % n])

        return res
