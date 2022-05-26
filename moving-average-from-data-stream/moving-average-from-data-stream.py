class MovingAverage:

    def __init__(self, size: int):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.head = 0
        self.count = 0
        self.sum = 0


    def next(self, val: int) -> float:
        #
        self.count += 1
        tail = (self.head + 1)% self.size
        self.sum = self.sum - self.queue[tail] + val
        self.head = (self.head + 1)%self.size
        self.queue[self.head] = val
        return self.sum / min(self.count,self.size)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)