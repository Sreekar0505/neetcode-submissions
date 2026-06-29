class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] if nums[i] > 0 else 0
        print (nums)

        for i in nums:
            if abs(i)-1 >= 0 and abs(i)-1 < len(nums):
                if nums[abs(i)-1] == 0:
                    nums[abs(i)-1] = 1
                nums[abs(i)-1] = -1*(abs(nums[abs(i)-1]))
        print (nums)
        
        for i in range(1,len(nums)+1):
            if nums[i-1] == abs(nums[i-1]):
                return i
        return len(nums)+1
        
