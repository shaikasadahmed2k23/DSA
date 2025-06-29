class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)  
        self.group = defaultdict(list)
        self.maxfreq = 0
    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]
        if f>self.maxfreq:
            self.maxfreq = f
        self.group[f].append(val)

    def pop(self) -> int:
        # val = self.group[self.maxfreq].pop()
        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()