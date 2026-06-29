class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        maxL, maxR = height[l], height[r]

        ans = 0
        while l<r:
            if maxL < maxR:
                l+=1
                water = maxL - height[l]
                if water > 0:
                    ans += water
                maxL = max(maxL,height[l])
            else:
                r-=1
                water = maxR - height[r]
                if water > 0:
                    ans += water
                maxR = max(maxR,height[r])
        return ans