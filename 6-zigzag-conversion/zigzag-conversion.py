class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        i = 0
        direction = 1

        for ch in s:
            rows[i] += ch

            if i == 0:
                direction = 1
            elif i == numRows - 1:
                direction = -1

            i += direction

        return "".join(rows)
