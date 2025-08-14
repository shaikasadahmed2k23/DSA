class Solution:
    def reverseBits(self, n: int) -> int:
        # x = bin(n)
        # print(x[::-1])
        # x = (x[2:])
        x = bin(n)[2:].zfill(32)

        # print(x)
        x = x[::-1]
        # print(x)
        return int(x,2)
        # return bin(x,2)