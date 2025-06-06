class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1 = int(a,2)
        b1 = int(b,2)
        c = a1+b1
        c1 = bin(c)
        c1 = c1[2:]
        return c1
        # print(a1)
        # a1 = bin(int(a))
        # a1 = a1[2:]
        # b1 = bin(int(b))
        # b1 = b1[2:]
        # # print(a1+)
        # c = a1+b1
        # a1 = int(a1)
        # print(a1)
        # return str(c)