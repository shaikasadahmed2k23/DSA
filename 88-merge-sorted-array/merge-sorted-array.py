class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n] = nums2
        nums1.sort()
        
        # nums1.extend(nums2)
        # # print(nums1)
        # nums1.sort()
        # # print(nums1)
        # finalen = len(nums1)
        # nums1 = nums1[finalen-(m+n):]
        
        # nums1 = nums1[m+n:]
        # print(nums1)