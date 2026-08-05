class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        dup = set()
        st = set()
        n = len(nums)
        for i in range(n):
            if nums[i] in dup:
                continue
            else:
                dup.add(nums[i])

                target = 0 - nums[i]
                l = i + 1
                h = n - 1
                while l < h:
                    sm = nums[l] + nums[h]
                    if sm == target:
                        st.add((nums[i],nums[l],nums[h]))
                        l += 1
                        h -= 1
                    elif sm < target:
                        l += 1
                    else:
                        h -= 1
        return [list(x) for x in st]


#         [-4, -1, -1, 0, 1, 2]

# -4 + x + y = 0
# x + y = 0 -(-4)
# x + y = 4
# search in remaining array except i

# x + y = 1
# -4 2 = 2
# -4 1 = 3
# -4 1 = -3
# -1 1 = 0
# done? l++ cuz chota number hi chahiye
# -1 + 1 = 0

# for i in range len(nums):
#     s = 0 - nums[i]
#     l = 0 
#     h = len(nums) - 1
#     while l < h:
#         sm = nums[l] + nums[h]
#         if sm == target and l != i and h != i:
#             set.add([nums[i],nums[l],nums[h]])
#             l += 1
#         elif sm < target:
#             l += 1
#         else:
#             h -= 1
# return set(with values)