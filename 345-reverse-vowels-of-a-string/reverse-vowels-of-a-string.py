class Solution:
    def reverseVowels(self, s: str) -> str:
        # for i in range(len(s)//2):
        vow = 'aeiouAEIOU'
        v1 = []
        for i in range(len(s)):
            if s[i] in vow:
                v1.append(s[i])
        # print(v1)
        v1 = v1[::-1]
        idx = 0
        s1 = list(s)
        for i in range(len(s)):
            if s[i] in vow:
                s1[i] = v1[idx]
                idx += 1
        # print(s1)
        # print(str(s1))
        return "".join(s1)