class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        o = []
        e = []

        st = str(num)

        for ch in st:
            d = int(ch)
            if d % 2 == 0:
                e.append(d)
            else:
                o.append(d)

        o.sort(reverse=True)
        e.sort(reverse=True)

        oi = ei = 0
        s = ""

        for ch in st:
            d = int(ch)

            if d % 2 == 0:
                s += str(e[ei])
                ei += 1
            else:
                s += str(o[oi])
                oi += 1

        return int(s)