class Edge:
    def __init__(self,a,b,cost):
        self.a = a
        self.b = b
        self.cost = cost

    def __lt__(self,other):
        return self.cost < other.cost	

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        src = 0
        n = len(points)
        pq = []
        
        def costFunction(a,b):
            a_x,a_y = points[a]
            b_x,b_y = points[b]
            return abs(a_x - b_x) + abs(a_y - b_y)
        
        for i in range(n):
            pq.append(Edge(0,i,costFunction(0,i)))

        heapq.heapify(pq)
        visited = set()
        min_cost = 0
        count = n - 1
        while pq and count >= 0:
            edge = heapq.heappop(pq)
            src = edge.a
            dest = edge.b
            cost = edge.cost
            if dest in visited:
                continue
            min_cost += cost
            visited.add(dest)
            count -= 1

            for neigh in range(n):
                if neigh not in visited:
                    heapq.heappush(pq,Edge(dest,neigh,costFunction(dest,neigh)))

        return min_cost
