class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        dup = set()
        n = len(nums)

        ans = nums[0] + nums[1] + nums[2]

        for i in range(n):

            if nums[i] in dup:
                continue

            dup.add(nums[i])

            rem = target - nums[i]

            l = i + 1
            h = n - 1

            while l < h:

                sm = nums[l] + nums[h]

                if abs((nums[i] + sm) - target) < abs(ans - target):
                    ans = nums[i] + sm

                if sm < rem:
                    l += 1
                elif sm > rem:
                    h -= 1
                else:
                    return target

        return ans
        # nums = sorted(nums)
        # dup = set()
        # ans = set()
        # n = len(nums)
        # ans = nums[0] + nums[1] + nums[2]

        # for i in range(len(nums)):
        #     if nums[i] in dup:
        #         continue
        #     else:
        #         dup.add(nums[i])

        #         target -= nums[i]

        #         l = i + 1
        #         h = n - 1

        #         while l < h:

        #             sm = nums[l] + nums[h]

        #             if abs((nums[i] + sm) - target) < abs(ans - target):
        #                 ans = nums[i] + sm

        #             if sm < rem:
        #                 l += 1
        #             elif sm > rem:
        #                 h -= 1
        #             else:
        #                 return target

        #     return ans