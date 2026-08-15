class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        m = 0
        h = len(nums) - 1
        while m <= h:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            elif nums[m] == 2:
                nums[m], nums[h] = nums[h], nums[m]
                h -= 1


        # # return nums.sort
        # z = []
        # o = []
        # t = []
        # for i in nums:
        #     if i == 0:
        #         z.append(0)
        #     elif i == 1:
        #         o.append(1)
        #     else:
        #         t.append(2)
        # # print(z,o,t)
        # z.extend(o)
        # z.extend(t)
        # # return str(z).replace(" ", "")
        # # print(z)
        # nums[:] = z
        
        # # return z