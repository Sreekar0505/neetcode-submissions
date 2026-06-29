class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        last = nums[0]
        i = 0
        while nums[i] != 0:
            last = nums[i]
            nums[i] = 0
            i = last
        return last