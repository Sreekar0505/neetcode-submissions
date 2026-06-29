class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)
        stack = []
        for p,s in pair:
            curr = (target-p)/s
            if len(stack) >= 1 and curr <= stack[-1]:
                #do nothing
                print(curr)
            else:
                stack.append(curr)
        return len(stack)