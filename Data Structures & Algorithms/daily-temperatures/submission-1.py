class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        res = [0]*n
        stack = []

        for i in range(n):
            while len(stack)>0 and stack[-1][0] < temp[i]:
                res[stack[-1][1]] = i-stack[-1][1]
                stack.pop()
            stack.append([temp[i], i])
        return res
