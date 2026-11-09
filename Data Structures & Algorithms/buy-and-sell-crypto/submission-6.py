class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = float('inf')

        for num in prices:
            min_buy = min(min_buy, num)
            max_profit = max(max_profit, num - min_buy)
        
        return max_profit