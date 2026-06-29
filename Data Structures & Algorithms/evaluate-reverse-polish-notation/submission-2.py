class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+' or i == '-' or i == '*' or i == '/':
                val = stack[-1]
                stack.pop()
                stack[-1] = str(int(eval(stack[-1] + i + val)))
            else:
                stack.append(i)
        return int(stack[-1])