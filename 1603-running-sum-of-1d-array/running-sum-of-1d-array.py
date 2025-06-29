class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        if len(nums) == 1:
            return nums
            
        if len(nums)>1:
            res.append(nums[0])
        for i in range(1,len(nums)):
            res.append(res[-1]+nums[i])
        return res
