class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.size = 0

    def push(self, x: int) -> None:
     
        self.stack.append(x)
        self.size += 1
        
    def pop(self) -> None:
        temp = self.stack.pop()
        self.size -= 1


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
