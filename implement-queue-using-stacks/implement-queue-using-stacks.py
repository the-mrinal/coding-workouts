class MyQueue:

    def __init__(self):
        self.stackPush = []
        self.stackPop = []
        
        

    def push(self, x: int) -> None:
        while self.stackPop:
            self.stackPush.append(self.stackPop.pop())
        self.stackPush.append(x)

    def pop(self) -> int:
        while self.stackPush:
            self.stackPop.append(self.stackPush.pop())
        
        return self.stackPop.pop()
        

    def peek(self) -> int:
        while self.stackPush:
            self.stackPop.append(self.stackPush.pop())
        
        return self.stackPop[-1]
        

    def empty(self) -> bool:
        if self.stackPush or self.stackPop:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()