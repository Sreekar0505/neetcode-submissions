class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        var = 1
        for i in range(len(nums)-1):
            res[i+1] = res[i+1] * nums[i] * var
            var *= nums[i]

        var = 1
        for i in range(len(nums)-1,0, -1):
            res[i-1] = res[i-1] * nums[i] * var
            var *= nums[i]

        return res

        