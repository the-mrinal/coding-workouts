# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         dist = [ float('inf') for _ in range(n)]
        
#         dist[k - 1] = 0
        
#         for i in range(n):
#             for src,dest,time in times:
#                 if dist[dest - 1] > dist[src - 1] + time:
#                     dist[dest - 1] = dist[src - 1] + time
        
#         return max(dist) if max(dist) < float('inf') else -1
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # using min heap
        adjMap = defaultdict(list)
        for src,dest,weight in times:
            adjMap[src].append((dest,weight))
        
        
        dist  = [float('inf') for i in range(n)]
        
        dist[k - 1] = 0
        
        pq = [(0,k)]
        
        heapq.heapify(pq)
        
        while pq:
            w , src = heapq.heappop(pq)
            
            for dest,d_weight in adjMap[src]:
                if dist[dest - 1] > dist[src - 1] + d_weight:
                    dist[dest - 1] = dist[src - 1] + d_weight
                    heapq.heappush(pq,(dist[dest - 1],dest))
        
        return max(dist) if max(dist) < float('inf') else -1
        
        