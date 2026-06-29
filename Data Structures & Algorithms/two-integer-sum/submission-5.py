class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            if k-nums[i] in visited:
                return [visited[k-nums[i]],i]
            visited[nums[i]] = i
        return [-1,-1]
