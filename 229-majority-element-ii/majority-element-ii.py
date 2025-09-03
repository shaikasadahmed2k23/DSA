class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x = len(nums)//3
        f = {}
        r = []
        for i in nums:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        for k,v in f.items():
            if v>x:
                # return v
                r.append(k)
        return r