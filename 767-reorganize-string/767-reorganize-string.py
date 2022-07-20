class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = collections.Counter(s)
        maxHeap = []
        
        for val,count in freq.items():
            heappush(maxHeap,(-count,val))

            
        res = []
        prevCount = 0
        prev = None
        while maxHeap:
            curr_count,curr = heappop(maxHeap)
            
            res.append(curr)
            
            if -prevCount > 0 and prev:
                heappush(maxHeap,(prevCount,prev))
            
            prev = curr
            prevCount = curr_count + 1
        
        return ''.join(res) if len(res) == len(s) else ""