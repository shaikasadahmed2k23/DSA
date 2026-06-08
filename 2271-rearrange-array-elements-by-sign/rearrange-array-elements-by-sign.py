class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = []
        n = []
        for i in nums:
            if i > 0:
                p.append(i)
            else:
                n.append(i)
        idx = 0
        ans = []
        for j in p:
            ans.append(j)
            ans.append(n[idx])
            idx += 1
        # print(ans)
        return ans
        