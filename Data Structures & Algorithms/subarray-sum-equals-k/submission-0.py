class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preFix = {0: 1}
        ans = 0
        summ = 0
        for i in nums:
            summ += i
            if summ-k in preFix:
                ans+=preFix[summ-k]
            preFix[summ] = preFix.get(summ,0) + 1
        return ans