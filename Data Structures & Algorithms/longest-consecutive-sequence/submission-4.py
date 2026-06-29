class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = 1
        
        i=0
        maxi = 0
        while i<len(nums):
            if nums[i]-1 not in dic:
                k = nums[i]
                while k in dic:
                    k+=1
                maxi = max(maxi,k-nums[i])
            i+=1
        return maxi