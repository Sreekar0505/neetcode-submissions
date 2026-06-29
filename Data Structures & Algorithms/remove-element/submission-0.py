class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        i=0
        while i<len(nums):
            if nums[i] != val:
                count+=1
            else:
                nums.pop(i)
                i-=1
            i+=1
        return count