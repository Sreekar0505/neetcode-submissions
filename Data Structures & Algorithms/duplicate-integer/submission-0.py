class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = {}
        for i in nums:
            if i in visited:
                return True
            if i not in visited:
                visited[i] = 1
        return False    