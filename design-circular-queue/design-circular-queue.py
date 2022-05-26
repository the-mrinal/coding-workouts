class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None for i in range(k)]
        self.size = k
        self.head = 0
        self.tail = 0
        

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            # insert 
            self.queue[self.tail] =  value
            self.tail = (self.tail + 1) % self.size
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        if not self.isEmpty():
            # remove
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.size
            return True
        else:
            return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.head]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.tail - 1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.head == self.tail and self.queue[self.head] == None:
            return True
        return False

    def isFull(self) -> bool:
        if self.head == self.tail and self.queue[self.head] != None:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()