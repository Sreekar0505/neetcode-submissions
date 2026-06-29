class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        idx = -1
        product = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros+=1
                idx=i
            else:
                product*= nums[i]
        if zeros > 1:
            return [0]*len(nums)
        if zeros == 1:
            ans = [0]*len(nums)
            ans[idx] = product
            return ans
        return [(product)//x for x in nums]