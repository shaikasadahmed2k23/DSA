class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        # This set will store all unique OR values found across all subarrays.
        res = set()
        
        # This set stores the distinct ORs of all subarrays ending at the previous position.
        crs = set()

        # Iterate through each element of the array.
        for x in arr:
            # `nrs` will store the ORs of subarrays ending at the current element `x`.
            # It's calculated by OR-ing x with all values in `crs`,
            # and adding x itself (for the subarray of length 1).
            nrs = {x | y for y in crs}
            nrs.add(x)
            
            # Add all newly found ORs for subarrays ending at x to the main result set.
            res.update(nrs)
            
            # For the next iteration, the current results become the previous results.
            crs = nrs
            
        return len(res)