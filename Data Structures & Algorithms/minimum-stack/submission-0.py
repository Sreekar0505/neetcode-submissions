class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = 99999999999
        

    def push(self, val: int) -> None:
        self.minVal = min(self.minVal,val)
        self.stack.append([val,self.minVal])

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
            if len(self.stack) > 0:
                self.minVal = self.stack[-1][1]
            else:
                self.minVal = 99999999999
        

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][0]
        return -1
        

    def getMin(self) -> int:
        return self.minVal 

        
