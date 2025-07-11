class Solution:
    def findLHS(self, nums):
        nums.sort()
        j = 0
        ml = 0

        for i in range(len(nums)):
            while nums[i] - nums[j] > 1:
                j += 1
            if nums[i] - nums[j] == 1:
                ml = max(ml, i - j + 1)
        return ml