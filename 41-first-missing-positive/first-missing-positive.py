class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 1) Replcaing -ve elements with n+2
        n = len(nums)
        # x = n+2
        for i in range(n):
            # n = len(nums)
            if nums[i]<=0 or nums[i]>n:
                nums[i] = n+1
        # print(nums)
        for i in range(n):
            v = abs(nums[i])
            if v<=n and nums[v-1]>0:
                nums[v-1] = -nums[v-1] 
            # nums[nums[i]-1] = (-1)*(nums[i])
        # print(nums)
        for j in range(n):
            if nums[j]>0:
                return j+1
        return n+1
        # return 1
        
