class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap,-num)
        else:
            heappush(self.minHeap,num)

        self.rebalance_heaps()


    def rebalance_heaps(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap,-heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap,-heappop(self.minHeap))

    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            meadian = -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
            return meadian
        return -self.maxHeap[0] / 1.0

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()