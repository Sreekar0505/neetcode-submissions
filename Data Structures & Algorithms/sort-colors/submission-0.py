class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        for i in nums:
            if i == 0:
                zeros+=1
            elif i == 1:
                ones+=1
        for i in range(len(nums)):
            if zeros == 0 and ones == 0:
                nums[i] = 2
            elif zeros == 0:
                nums[i] = 1
                ones-=1
            else:
                nums[i] = 0
                zeros-=1
        
