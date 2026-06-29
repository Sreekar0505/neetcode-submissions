class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,k = 0,0
        while i<len(nums) and k<len(nums):
            if i==0 or nums[i]>nums[i-1]:
                nums[k] = nums[i]
                i+=1
                k+=1
            else:
                i+=1
        nums = nums[:k]
        return len(nums)

