class Solution:
    def canBeTypedWords(self, t: str, bl: str) -> int:
        bl = set(bl)
        w = t.split(" ")
        cnt = 0
        for wr in w:
            for c in wr:
                if c in bl:
                    cnt += 1
                    break
        return len(w) - cnt