from typing import List
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq1 = Counter(basket1)
        freq2 = Counter(basket2)
        freq_total = freq1 + freq2
        
        # Check feasibility: each fruit count must be even
        for fruit, count in freq_total.items():
            if count % 2 != 0:
                return -1
        
        to_swap_from_basket1 = []
        to_swap_from_basket2 = []
        
        # Identify fruits that need to be swapped from each basket
        for fruit in freq_total:
            diff = freq1[fruit] - freq2[fruit]
            if diff > 0:
                to_swap_from_basket1.extend([fruit] * (diff // 2))
            elif diff < 0:
                to_swap_from_basket2.extend([fruit] * (-diff // 2))
        
        # Sort lists for optimal pairing
        to_swap_from_basket1.sort()
        to_swap_from_basket2.sort(reverse=True)
        
        min_fruit = min(freq_total.keys())
        cost = 0
        
        # Calculate total minimum cost
        for f1, f2 in zip(to_swap_from_basket1, to_swap_from_basket2):
            cost += min(min(f1, f2), 2 * min_fruit)
        
        return cost
