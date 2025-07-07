class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pf = strs[0]
        pl = len(pf)

        for s in strs[1:]:
            while pf != s[0:pl]:
                pl -= 1
                if pl == 0:
                    return ""
                
                pf = pf[0:pl]
        
        return pf