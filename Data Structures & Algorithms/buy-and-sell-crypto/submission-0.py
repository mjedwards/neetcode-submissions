class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        l = 1
        while l < len(prices):
            if prices[l] - min_price > max_profit:
                max_profit = prices[l] - min_price
            if prices[l] < min_price:
                min_price = prices[l]
            l+=1

        return max_profit
        