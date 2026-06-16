class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        n = len(s)
        for i in range(n):
            if s[i].isalpha():
                res += s[i]
            elif s[i] == '*':
                if res:
                    res = res[:len(res)-1]
            elif s[i] == '#':
                if res:
                    res += res
                
            elif s[i] == "%":
                res = res[::-1]
        return res