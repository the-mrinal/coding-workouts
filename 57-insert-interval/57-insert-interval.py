class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        minHeap = []
        for start,end in intervals + [newInterval]:
            heappush(minHeap,(start,-1))
            heappush(minHeap,(end,1))            
        
        curr = 0
        s = None
        res = []
        while minHeap:
            val,gate = heappop(minHeap)
            
            if s is None:
                s = val
            
            curr += gate
            if curr == 0:
                res.append([s,val])
                s = None
        return res