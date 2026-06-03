class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """

        def check(mat, i, j):
            if mat[i][j] == 0:
                return 0

            sm = 0

            for col in range(n):
                sm += mat[i][col]

            for row in range(m):
                sm += mat[row][j]
            sm -= 1

            return sm

        m = len(mat)
        n = len(mat[0])
        c = 0

        for i in range(m):
            for j in range(n):
                x = check(mat, i, j)
                if x == 1:
                    c += 1

        return c