class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjMap = defaultdict(list)
        for s,d,w in times:
            adjMap[s].append([w,d])

        dest = [float('inf') for i in range(n)]

        dest[k - 1] = 0 # due 0th indexed arr

        pq = [(0,k)]

        heapq.heapify(pq)

        while pq:
            w,curr = heapq.heappop(pq)
            for d_w,d in adjMap[curr]:
                if dest[d-1] > dest[curr - 1] + d_w:
                    dest[d - 1] = dest[curr - 1] + d_w
                    heapq.heappush(pq,(dest[d - 1],d))

        return max(dest) if max(dest) < float('inf') else -1
