class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def costF(a,b):
            xi,yi = points[a]
            xj,yj = points[b]
            return abs(xi - xj) + abs(yi - yj)
        
        if not points and len(points) == 0:
            return 0
        n = len(points)
        
        visited = [False] * n
        
        pq = []
        
        result = 0
        count = n - 1
        
        xi,yi = points[0]
        for i in range(1,n):
            xj,yj = points[i]
            pq.append(Edge(0,i,costF(0,i)))
        
        heapq.heapify(pq)
        
        visited[0] = True
        minCost = 0
        while pq and count > 0:
            edge = heapq.heappop(pq)
            i = edge.point1
            j = edge.point2
            cost = edge.cost
            
            if not visited[j]:
                minCost += cost
                visited[j] = True
                for i in range(n):
                    if not visited[i]:
                        xi,yi = points[j]
                        xj,yj = points[i]
                        new_cost = costF(j,i)
                        heapq.heappush(pq,Edge(j,i,costF(i,j)))
                count -= 1
        
        return minCost
        
        
        
class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost      
        
        
        