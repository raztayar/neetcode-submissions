class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        max_diff = 0
        lowest_i = 0

        while j < len(prices):
            if prices[j] - prices[i] >= max_diff:
                max_diff = prices[j] - prices[i]
                
            if prices[j] < prices[i]:
                i = j
            j += 1
        
        return max_diff