class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        minHeap = []
        count = 1
        for start,end in intervals:
            if minHeap:
                if minHeap and minHeap[0][0] <= start:
                    heappop(minHeap)
                heappush(minHeap,[end,start])
            else:
                heappush(minHeap,[end,start])
        return len(minHeap)