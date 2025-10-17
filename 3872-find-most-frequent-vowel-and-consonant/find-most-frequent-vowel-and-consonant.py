class Solution:
    def maxFreqSum(self, s: str) -> int:
        f = {}
        v = set('aeiou')
        for i in s:
            if i in f:
                # if i in v:
                f[i] += 1
            else:
                f[i] = 1
        # print(f)
        vow = cons = 0
        for k,c in f.items():
            if k in v:
                vow = max(c,vow)
            else:
                cons = max(c,cons)
        # print(vow,cons)
        return vow + cons

        