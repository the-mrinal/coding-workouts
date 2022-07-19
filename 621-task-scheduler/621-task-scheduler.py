class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        maxHeap = []
        
        for val,count in freq.items():
            heappush(maxHeap,(-count,val))
        
        que = deque()
        
        time = 0
        timeTaken = 0
        while maxHeap:
            wait = []
            k = n + 1
            while k > 0 and maxHeap:
                count,val = heappop(maxHeap)
                timeTaken += 1
                
                wait.append((count + 1,val))
                k -= 1
            
            for count,val in wait:
                if -count > 0:
                    heappush(maxHeap,(count,val))
            
            if maxHeap:
                timeTaken += k
        
        return timeTaken