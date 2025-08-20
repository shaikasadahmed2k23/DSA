class Solution:
    def reverseWords(self, s: str) -> str:

        x = s.split(' ')
        # s1 = ""
        s1 = []
        for i in x:
            s1.append(i[::-1])
        # print(s1)
        return " ".join(s1)
        # return s1