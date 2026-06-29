class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [x for x in height]
        suffix = [x for x in height]
        n = len(height)

        for i in range(1,n):
            prefix[i]=max(prefix[i-1],prefix[i])
        for i in range(n-2,-1,-1):
            suffix[i]=max(suffix[i+1],suffix[i])
        ans = 0
        for i in range(1,n-1):
            ans += max(0,min(prefix[i-1],suffix[i+1])-height[i])
        return ans
