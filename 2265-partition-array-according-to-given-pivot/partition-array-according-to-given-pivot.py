class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        lar = []
        rar = []
        c = 0
        for i in nums:
            if i < pivot:
                lar.append(i)
            elif i == pivot:
                c += 1
            else:
                rar.append(i)
        # print
        ans = []
        for j in lar:
            ans.append(j)
        for i in range(c):
            ans.append(pivot)
        # for i in range()
        # rar.sort()
        ans.extend(rar)
        return ans