class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        prev = [float('inf')] * n
        curr = [float('inf')] * n

        prev[src] = 0

        for i in range(1,k + 2):
            curr[src] = 0
            for flight in flights:
                prev_flight,curr_flight,cost = flight
                if prev[prev_flight] < float('inf'):
                    curr[curr_flight] = min(curr[curr_flight],prev[prev_flight] + cost)
            prev = curr.copy()
        return -1 if curr[dst] == float('inf') else curr[dst]
