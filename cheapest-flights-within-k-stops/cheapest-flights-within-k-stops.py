class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # we will have to make 2 queues - prev and curr
        print(src,dst,k)
        prev = [float('inf') for _ in range(n)]
        curr = [float('inf') for _ in range(n)]
        
        prev[src] = 0
        
        for i in range(1,k + 2):
            
            curr[src] = 0
            
            for s,d,dist in flights:
                if curr[d] > prev[s] + dist:
                    curr[d] = prev[s] + dist
            print(curr)
            prev = curr.copy()
            
        return prev[dst] if prev[dst] < float('inf') else -1
            
            