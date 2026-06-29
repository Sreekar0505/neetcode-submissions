class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r = 0
        add = 0
        ans = len(nums)+1
        for l in range(len(nums)):
            while r<len(nums) and add < target:
                add+=nums[r]
                r+=1
            if (add >= target):
                ans = min(ans,r-l)
            add -= nums[l]
        return ans if ans != len(nums) + 1 else 0
            