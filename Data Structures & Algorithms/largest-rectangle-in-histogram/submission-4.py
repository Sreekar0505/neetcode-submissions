class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = -1
        for ind, val in enumerate(heights):
            start = ind
            while (len(stack) != 0 and stack[-1][1] > val):
                maxArea = max(maxArea, (ind - stack[-1][0])*(stack[-1][1]))
                start = stack[-1][0]
                stack.pop()
            stack.append([start,val])
        
        for ind, val in stack:
            maxArea = max(maxArea, (len(heights) - ind)*(val))
        
        return maxArea