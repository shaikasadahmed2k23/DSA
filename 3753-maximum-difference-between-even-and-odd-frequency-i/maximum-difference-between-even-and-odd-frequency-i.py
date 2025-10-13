class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd = [c for c in freq.values() if c % 2 != 0]
        even = [c for c in freq.values() if c % 2 == 0]
        
        diffs = []
        for o in odd:
            for e in even:
                diffs.append(o - e)
        
        return max(diffs) if diffs else 0
