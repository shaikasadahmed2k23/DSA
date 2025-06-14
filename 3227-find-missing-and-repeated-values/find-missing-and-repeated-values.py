from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = {}
        dup = -1
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                num = grid[i][j]
                if num in seen:
                    dup = num
                seen[num] = seen.get(num, 0) + 1

        total = n * m
        missing = -1
        for i in range(1, total + 1):
            if i not in seen:
                missing = i
                break

        return [dup, missing]
