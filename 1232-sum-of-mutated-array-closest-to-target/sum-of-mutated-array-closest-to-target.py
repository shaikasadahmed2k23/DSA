class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        l = 1
        r = max(arr)

        while l <= r:
            m = (l + r) // 2
            s = sum(min(a, m) for a in arr)

            if s < target:
                l = m + 1
            else:
                r = m - 1

        s1 = sum(min(a, r) for a in arr)
        s2 = sum(min(a, l) for a in arr)

        if abs(s1 - target) <= abs(s2 - target):
            return r
        return l