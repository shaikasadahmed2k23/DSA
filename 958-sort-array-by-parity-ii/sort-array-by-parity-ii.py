class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        o = []
        e = []
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                e.append(nums[i])
            else:
                o.append(nums[i])
        e.sort()
        o.sort()
        o = o[::-1]
        res = []
        idx1,idx2 = 0,0
        # while idx < len(nums):
        for i in range(len(nums)):
            if i%2 == 0:
                res.append(e[idx1])
                idx1 += 1
            else:
                res.append(o[idx2])
                idx2 += 1
        return res