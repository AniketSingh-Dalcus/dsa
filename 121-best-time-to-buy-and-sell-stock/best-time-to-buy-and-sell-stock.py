class Solution(object):
    def maxProfit(self, prices):
        max_price=0
        min_price=float("inf")
        n=len(prices)
        for i in range(0,n):
            min_price=min(min_price,prices[i])
            max_price=max(max_price,prices[i]- min_price)
        return max_price