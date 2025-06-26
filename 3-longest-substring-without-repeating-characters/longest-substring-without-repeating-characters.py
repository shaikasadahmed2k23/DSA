class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        df = set()
        l = 0
        ml = 0

        for r in range(len(s)):
            while s[r] in df:
                df.remove(s[l])
                l += 1
            df.add(s[r])
            ml = max(ml, r - l + 1)

        return ml

        
        # n = len(s)
        # if s == "":
        #     return 0
        # if s == " " or len(s) == 1  :
        #     return 1
        # if len(s) == 2:
        #     if len(set(list(s))) == 2:
        #         return 2
        # ml = -(1<<31)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         x = s[i:j]
        #         f = {}
        #         for k in x:
        #             if k in f:
        #                 f[k] += 1
        #             else:
        #                 f[k] = 1
        #         if len(f) == len(x):
        #             ml = max(ml,len(f))
        #         # print(x)
        # return ml