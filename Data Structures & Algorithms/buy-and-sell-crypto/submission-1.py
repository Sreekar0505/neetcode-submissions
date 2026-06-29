class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        ret = 0
        for i in prices:
            ret = max(ret, i-mini)
            mini = min(mini, i)
        return ret