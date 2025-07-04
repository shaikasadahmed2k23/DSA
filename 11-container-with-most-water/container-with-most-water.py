class Solution:
    def maxArea(self, height: List[int]) -> int:
        mxar = 0
        n = len(height)
        p1 = 0
        p2 = n - 1
        while p1 < p2:
            curAr = min(height[p1] , height[p2]) *(p2-p1)
            mxar = max(curAr,mxar)
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return mxar    