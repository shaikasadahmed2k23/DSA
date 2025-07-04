class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        x = list(set(nums))
        # print(len(x))
        x.sort()
        for i in range(len(x)):
            nums[i] = x[i]
        
        return len(x)
        # # return len(x),list(x)