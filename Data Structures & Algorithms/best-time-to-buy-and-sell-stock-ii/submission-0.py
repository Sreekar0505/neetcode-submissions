class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        flag = prices[0]
        prices.append(max(prices)+1)
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[i-1]:
                profit += prices[i-1]-flag
                flag = prices[i]
            else:
                profit += prices[i-1]-flag
                flag = prices[i-1]
        return profit
            
            