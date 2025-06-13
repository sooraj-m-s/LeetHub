class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = prices[0], 0
        for i in prices:
            if i < min_price:
                min_price = i
            else:
                max_profit = max(max_profit, i - min_price)
        return max_profit