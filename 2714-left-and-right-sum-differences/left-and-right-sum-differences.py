class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ls = rs = 0
        lsa = []
        rsa = []
        lsa.append(ls)
        rsa.append(rs)
        n = len(nums)
        m = n-1
        for i in range(m):
            ls += nums[i]
            lsa.append(ls)
            rs += nums[n-i-1]
            rsa.append(rs)
        x = []
        rsa.reverse()
        mm = len(rsa)
        for i in range(mm):
            y = abs(rsa[i] - lsa[i])
            x.append(y)

        return x
        # print(lsa)
        # print(rsa)
        # return [0,1]

# 10 3 8 3
# 0  1 2 3 
# ls += arr[i] + arr[i+1]
# rs += arr[n-i]    