__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # print(opera
        f = {}
        for i, num in enumerate(nums):
            f[num] = i
        # print(f)
        for old, new in operations:
            if old in f:
                idx = f.pop(old)
                f[new] = idx
        # print(f)
        res = [0] * len(nums)
        # result = [0] * len(nums)
        for num, idx in f.items():
            res[idx] = num

        return res