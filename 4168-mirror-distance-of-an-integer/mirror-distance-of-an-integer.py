class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        rev = str(n)[::-1]
        m = int(rev)
        # print(m)...
        return abs(m-n)