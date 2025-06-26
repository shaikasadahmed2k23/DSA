from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float('inf')
        mxp = 0

        for price in prices:
            if price < minp:
                minp = price
            elif price - minp > mxp:
                mxp = price - minp

        return mxp
