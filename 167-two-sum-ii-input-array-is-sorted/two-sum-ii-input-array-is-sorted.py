class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        h = len(numbers) - 1 
        while l < h:
            s = numbers[l] + numbers[h]
            if(s == target):
                return [l+1,h+1]
            elif s < target:
                l += 1
            else:
                h -= 1