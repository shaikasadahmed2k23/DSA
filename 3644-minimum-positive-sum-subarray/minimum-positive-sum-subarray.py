
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')

        for i in range(len(nums)):
            s = 0

            for j in range(i, len(nums)):
                s += nums[j]
                length = j - i + 1

                if l <= length <= r and s > 0:
                    ans = min(ans, s)

        if ans == float('inf'):
            return -1

        return ans

