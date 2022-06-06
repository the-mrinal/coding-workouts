class Edge:
	def __init__(self,a,b,cost):
		self.a = a
		self.b = b
		self.cost = cost
	
	def __lt__(self,other):
		return self.cost < other.cost
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def cost(a,b):
            xi,yi = points[a]
            xj,yj = points[b]
            return abs(xi - xj) + abs(yi - yj)
		
        
        min_heap = []
        n = len(points)
        for i in range(1,n):
            edge = Edge(0,i,cost(0,i))
            min_heap.append(edge)
        
        heapq.heapify(min_heap)
        visited = set()
        visited.add(0)
        min_cost = 0
        
        count = n - 1 
        while min_heap and count > 0:
            edge = heapq.heappop(min_heap)
            
            if edge.b not in visited:
                min_cost += edge.cost
                visited.add(edge.b)
                for neigh in range(n):
                    if neigh not in visited:
                        heapq.heappush(min_heap,Edge(edge.b,neigh,cost(edge.b,neigh)))
                count -= 1

        return min_cost