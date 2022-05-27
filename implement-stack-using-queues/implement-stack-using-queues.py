class MyStack:

    def __init__(self):
        self.q1 = deque([])
        self.q2 = deque([])
        

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        popItem = None
        while self.q1:
            popItem = self.q1.popleft()
            self.q2.append(popItem)
        
        while self.q2:
            curr = self.q2.popleft()
            if popItem == curr:
                continue
            self.q1.append(curr)
        return popItem

    def top(self) -> int:
        popItem = None
        while self.q1:
            popItem = self.q1.popleft()
            self.q2.append(popItem)
        
        while self.q2:
            curr = self.q2.popleft()
            self.q1.append(curr)
        
        return popItem

    def empty(self) -> bool:
        if self.q1:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()