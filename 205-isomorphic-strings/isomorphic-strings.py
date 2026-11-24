class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return ""
        fst = {}
        n = len(s)
        for i in range(n):
            # if s[i] not in f:
            #     f[s[i]] = t[i]
            if s[i] in fst:
                if fst[s[i]] != t[i]:
                    return False 
            if t[i] in fst.values():
                if s[i] not in fst:
                    return False
            fst[s[i]] = t[i]

        return True
            