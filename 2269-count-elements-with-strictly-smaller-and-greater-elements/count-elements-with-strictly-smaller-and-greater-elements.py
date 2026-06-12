class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1 or len(set(nums)) == 1:
            return 0
        return  len(nums) - nums.count(min(nums)) - nums.count(max(nums))