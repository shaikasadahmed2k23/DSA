class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        res = []
        s = []
        for i in range(n-1,-1,-1):
            while s:
                if t[i]>=t[s[-1]]:
                    s.pop()
                else:
                    break
            # s.append(t[i])
            if s:
                c = s[-1] - i
                res.append(c)
                # res.append(0)
            else:
                res.append(0)
            s.append(i)
        return res[::-1]


        
        #     c = 0
        #     f = 0
        #     for j in range(i+1,n):
        #         c += 1
        #         if t[j] > t[i]:
        #             res.append(c)
        #             f = 1
        #             break
        #         # c += 1
        #     if f == 0:
        #         res.append(0)
        # return res