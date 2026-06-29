class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax, rightMax = [0] * n, [0] * n

        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1],height[i-1])
            rightMax[n-1-i] = max(rightMax[n-i],height[n-i])
        
        ans = 0

        for i in range(n):
            diff = min(leftMax[i], rightMax[i]) - height[i]
            if diff > 0:
                ans += diff

        return ans