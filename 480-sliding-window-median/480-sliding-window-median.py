class Solution:
    def  __init__(self):
        self.maxHeap = []
        self.minHeap = []
    
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = [0.0 for i in range(len(nums) - k + 1)]
        n = len(nums)
        for i in range(n):
            if not self.maxHeap or -self.maxHeap[0] >= nums[i]:
                heappush(self.maxHeap,-nums[i])
            else:
                heappush(self.minHeap,nums[i])

            self.rebalance_heaps()

            if i - k + 1 >= 0:
                if len(self.maxHeap) == len(self.minHeap):
                    res[i-k+1] = -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
                else:
                    res[i-k+1] =-self.maxHeap[0] / 1.0

                elemToRemove = nums[i - k + 1]
                if elemToRemove <= -self.maxHeap[0]:
                    self.remove(self.maxHeap,-elemToRemove)
                else:
                    self.remove(self.minHeap,elemToRemove)

                self.rebalance_heaps()
            
        return res

    def rebalance_heaps(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap,-heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap,-heappop(self.minHeap))

    def remove(self,heap,elem):
        ind = heap.index(elem)
        heap[ind] = heap[-1]

        del heap[-1]
        if ind < len(heap):
            heapq._siftup(heap,ind)
            heapq._siftdown(heap,0,ind)
        #heapify(heap)
