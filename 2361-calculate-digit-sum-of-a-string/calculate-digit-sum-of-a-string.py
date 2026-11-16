
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            ans = ""

            for i in range(0, len(s), k):
                x = 0

                for j in range(i, min(i + k, len(s))):
                    x += int(s[j])

                ans += str(x)

            s = ans

        return s
