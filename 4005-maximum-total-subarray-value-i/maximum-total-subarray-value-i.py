class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_val = max(nums)
        min_val = min(nums)
        return k * (max_val - min_val)