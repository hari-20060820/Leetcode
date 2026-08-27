class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minStack or value <=self.minStack[-1]:
            self.minStack.append(value)
    def pop(self) -> None:
        if not self.stack :
            return 
        else:
            
            value= self.stack.pop()
            if value==self.minStack[-1]:
                self.minStack.pop()
            

    def top(self) -> int:
        if not self.stack:
            return 
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        if not self.minStack:
            return 
        else:
            return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()