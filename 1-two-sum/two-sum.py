class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in nums:
        #     #print(i)
        #     x = abs(target-i)
        #     #print(x)
        #     if x in nums:
        #         z = nums.index(i)
        #         break
        # for j in range(0,len(nums)):
        #     if(nums[j] == x):
        #         y = j
        #         return (z,y)
        #     # if x in nums:
        #     #     return (nums.index(i),nums.index(x))
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] + nums[j] == target):
                    return (i,j)