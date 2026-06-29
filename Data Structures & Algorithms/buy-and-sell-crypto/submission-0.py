class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = 99999999999999
        ret = 0
        for i in prices:
            ret = max(ret, i-mini)
            mini = min(mini, i)
        return ret