class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)] 
        ml = 0
        for num in nums:
            crm = num % k
            for prvrm in range(k):
                dp[prvrm][crm] = dp[crm][prvrm] + 1
                ml = max(ml, dp[prvrm][crm])
        return ml