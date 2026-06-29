class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = -1

        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
                count = 1
            elif candidate == nums[i]:
                count +=1
            else:
                count-=1
        
        cnt = 0
        for i in nums:
            if i == candidate:
                cnt+=1
        return candidate if cnt >= len(nums)//2 else -1