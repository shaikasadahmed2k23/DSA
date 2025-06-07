class Solution(object):
    def wordPattern(self, p, s):
        w = s.split()
        if len(p) != len(w):
            return False

        a = {}
        b = {}

        for x, y in zip(p, w):
            if x in a:
                if a[x] != y:
                    return False
            else:
                a[x] = y

            if y in b:
                if b[y] != x:
                    return False
            else:
                b[y] = x

        return True
