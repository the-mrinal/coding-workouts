class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [ float('inf') for _ in range(n)]
        
        dist[k - 1] = 0
        
        for i in range(n):
            for src,dest,time in times:
                if dist[dest - 1] > dist[src - 1] + time:
                    dist[dest - 1] = dist[src - 1] + time
        
        return max(dist) if max(dist) < float('inf') else -1