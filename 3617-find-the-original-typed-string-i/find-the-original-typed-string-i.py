class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        c = n
        for i in range(1,n):
            if word[i] != word[i-1]:
                c -= 1
        return c