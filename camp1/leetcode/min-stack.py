class MinStack:
    def __init__(self):
        self.array = []
    def push(self, val: int) -> None:
        self.array.append(val)
    def pop(self) -> None:
        if len(self.array) == 0:
            return "can't pop from empty array"
        return self.array.pop()
    def top(self) -> int:
        if len(self.array) == 0:
            return "empty array"
        return self.array[-1]
    def getMin(self) -> int:
        return (sorted(self.array))[0]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()