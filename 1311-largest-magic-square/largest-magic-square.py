class Solution(object):
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])

        def isMagic(r, c, k):
            target = sum(grid[r][c:c+k])

            # rows
            for i in range(r, r+k):
                if sum(grid[i][c:c+k]) != target:
                    return False

            # cols
            for j in range(c, c+k):
                s = 0
                for i in range(r, r+k):
                    s += grid[i][j]
                if s != target:
                    return False

            # main diagonal
            s = 0
            for i in range(k):
                s += grid[r+i][c+i]
            if s != target:
                return False

            # anti diagonal
            s = 0
            for i in range(k):
                s += grid[r+i][c+k-1-i]
            if s != target:
                return False

            return True

        maxK = min(m, n)

        for k in range(maxK, 0, -1):
            for r in range(m-k+1):
                for c in range(n-k+1):
                    if isMagic(r, c, k):
                        return k

        return 1