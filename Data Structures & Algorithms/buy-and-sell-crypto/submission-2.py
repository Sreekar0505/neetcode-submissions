class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n=len(prices)
        prefix = [x for x in prices]
        for i in range(n-2,-1,-1):
            prefix[i] = max(prefix[i+1],prefix[i])
        for i in range(n):
            profit = max(profit, prefix[i]-prices[i])
        return profit