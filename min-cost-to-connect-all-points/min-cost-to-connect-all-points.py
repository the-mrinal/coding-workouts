class Edge:
    def __init__(self,a,b,cost):
        self.p1 = a
        self.p2 = b
        self.cost = cost
    
    def __lt__(self,other):
        return self.cost < other.cost


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        def costF(a,b):
            xi,yi = points[a]
            xj,yj = points[b]
            return abs(xi - xj) + abs(yi - yj)
        
        pq = []
        
        for j in range(1,n):
            pq.append(Edge(0,j,costF(0,j)))
        
        heapq.heapify(pq)
        
        visited = set([0])
        
        minCost = 0
    
        count = n - 1
        while len(visited) < n  and pq:
            edge = heapq.heappop(pq)
            print('ffg')
            if edge.p2 not in visited:            
                minCost += edge.cost
                visited.add(edge.p2)

                for j in range(n):
                    if j not in visited:
                        heapq.heappush(pq,Edge(edge.p2,j,costF(edge.p2,j)))
                count -= 1
        
        return minCost
        
        
        
            #     while count > 0  and pq:
            # edge = heapq.heappop(pq)
            # point1 = edge.p1
            # point2 = edge.p2
            # cost = edge.cost
            # if point2 not in visited:
            #     result += cost
            #     visited.add(point2)
            #     for j in range(n):
            #         if j not in visited:
            #             distance = abs(points[point2][0] - points[j][0]) + \
            #                        abs(points[point2][1] - points[j][1])
            #             heapq.heappush(pq, Edge(point2, j, distance))
            #     count -= 1
        
        
        