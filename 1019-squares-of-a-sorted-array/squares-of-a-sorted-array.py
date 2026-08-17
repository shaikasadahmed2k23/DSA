class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            x = nums[i] * nums[i]
            nums[i] = x
        # print(nums).
        y = sorted(nums)
        return y
        