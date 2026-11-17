
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0

        for i in arr1:
            far = True

            for j in arr2:
                if abs(i - j) <= d:
                    far = False
                    break

            if far:
                ans += 1

        return ans
