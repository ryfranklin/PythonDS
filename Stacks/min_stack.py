import stacks 

s = stacks.Stack()


class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.minNum = 0
        

    def push(self, val: int) -> None:
        if val < self.minNum:
            self.minNum = val
        return self.items.append(val)

    def pop(self) -> None:
        return self.items.pop()

    def top(self) -> int:
        return self.items[-1]
        

    def getMin(self) -> int:
        return self.minNum


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(val)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()