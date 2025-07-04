class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lin = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lin] = nums[i]
                lin += 1
        for i in range(lin,len(nums)):
            nums[i] = 0

        # if len(nums)>1:
        #     nums.sort()
        #     c = 0
        #     for i in range(len(nums)):
        #         if nums[i] == 0:
        #             c += 1
        #             # break
            
        #     # x = nums[c+1:]
        #     # y = nums[:c+1]
        #     # nums = x + y

        #     nums =  nums[:c+1] + nums[c+1:]