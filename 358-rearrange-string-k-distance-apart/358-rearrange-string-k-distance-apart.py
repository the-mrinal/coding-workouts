class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        freq = collections.Counter(s)
        maxHeap = []
        
        
        for val,count in freq.items():
            heappush(maxHeap,(-count,val))
        
        que = deque()
        result = []
        
        while maxHeap:
            count,val = heappop(maxHeap)
            result.append(val)
            
            que.append((count+1,val))
            if len(que) >= k:
                q_count,q_val = que.popleft()
                if -q_count > 0:
                    heappush(maxHeap,(q_count,q_val))
        
        return ''.join(result) if len(result) == len(s) else ""