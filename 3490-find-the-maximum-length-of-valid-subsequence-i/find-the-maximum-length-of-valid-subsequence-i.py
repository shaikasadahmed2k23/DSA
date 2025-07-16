class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ce = 0
        co = 0
        for num in nums:
            if num % 2 == 0:
                ce += 1
            else:
                co += 1
        
        edp = 0
        odp = 0
        for num in nums:
            if num % 2 == 0:
                edp = max(edp, odp + 1)
            else:
                odp = max(odp, edp + 1)
        
        return max(ce, co, edp, odp)