
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a: a[1])

        q = sorted(enumerate(queries), key=lambda a: a[1])

        ans = [0] * len(queries)
        d = {}

        l = 0
        r = 0

        for idx, t in q:
            while r < len(logs) and logs[r][1] <= t:
                s = logs[r][0]
                d[s] = d.get(s, 0) + 1
                r += 1

            while l < r and logs[l][1] < t - x:
                s = logs[l][0]
                d[s] -= 1

                if d[s] == 0:
                    del d[s]

                l += 1

            ans[idx] = n - len(d)

        return ans
