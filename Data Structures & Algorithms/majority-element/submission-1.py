class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = -1
        count = 0

        for i in range(len(nums)):
            if count == 0:
                count = 1
                candidate = nums[i]
            elif candidate == nums[i]:
                count+=1
            else:
                count-=1

        cnt = 0

        for i in nums:
            if i == candidate:
                cnt+=1
        if cnt >= len(nums)//2:
            return candidate
        return -1