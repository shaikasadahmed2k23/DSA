class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for i in operations:
            if i == 'C':
                s.pop()
            elif i == 'D':
                top = int(s[-1])
                s.append(2*top)
            elif i == '+':
                t1 = int(s[-1])
                t2 = int(s[-2])
                s.append(t1+t2)
            else:
                s.append(int(i))
        sm = 0
        # print(s)
        while s:
            tp = s[-1]
            # print(tp)
            sm += int(tp)
            s.pop()
        return sm