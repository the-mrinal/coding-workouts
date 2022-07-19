class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        kth_smallest = n - k + 1
        maxHeap = []
        for index,num in enumerate(nums):
            if index >= kth_smallest:
                if -maxHeap[0] >= num:
                    heappop(maxHeap)
                    heappush(maxHeap,-num)
            else:
                heappush(maxHeap,-num)
        print(maxHeap)
        return -maxHeap[0]
        