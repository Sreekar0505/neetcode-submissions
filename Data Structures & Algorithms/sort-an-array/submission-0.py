class Solution:
    def merge(self, num1, num2):
        i,j = 0,0
        res = []
        while i<len(num1) and j<len(num2):
            if num1[i] <= num2[j]:
                res.append(num1[i])
                i+=1
            else:
                res.append(num2[j])
                j+=1
        while i<len(num1):
            res.append(num1[i])
            i+=1
        while j<len(num2):
            res.append(num2[j])
            j+=1
        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        if (len(nums) == 0 or len(nums) == 1):
            return nums
        return self.merge(self.sortArray(nums[:len(nums)//2]),self.sortArray(nums[len(nums)//2:]))