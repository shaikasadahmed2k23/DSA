class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k +=1 
        return k
        # return list(set(nums))

#         x = set(nums)
#         # return list(x)
#         y = list(x)
#         # print(y)
#         # print(y
#         return len(x), y

# # [0,0,1,1,1,2,2,3,3,4]
# # l

# #         l = 0 
# #         h = 

