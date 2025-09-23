class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            x = nums[i:] + nums[:i]
            # print(x).
            if x == sorted(nums):
                return True
        return False