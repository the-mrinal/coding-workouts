class Edge:
	def __init__(self,a,b,cost):
		self.a = a
		self.b = b
		self.cost = cost
	
	def __lt__(self,other):
		return self.cost < other.cost

class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
        self.count = size
    
    def find(self,x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,a,b):
        rootA = self.find(a)
        rootB = self.find(b)
        
        if rootA == rootB:
            return
        
        if self.rank[rootA] > self.rank[rootB]:
            self.root[rootB] = rootA
        elif self.rank[rootA] < self.rank[rootB]:
            self.root[rootA] = rootB
        else:
            self.root[rootB] = rootA
            self.rank[rootA] += 1
        
        self.count -= 1
    
    def isConnected(self,a,b):
        return self.find(a) == self.find(b)
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def cost(a,b):
            xi,yi = points[a]
            xj,yj = points[b]
            return abs(xi - xj) + abs(yi - yj)
		
        n = len(points)
        
        min_heap = []
        for j in range(n):
            for i in range(j+1,n):
                edge = Edge(j,i,cost(j,i))
                min_heap.append(edge)
        
        heapq.heapify(min_heap)
        uf = UnionFind(n)
        count = n - 1
        min_cost = 0
        while min_heap and count > 0:
            edge = heapq.heappop(min_heap)
            
            if not uf.isConnected(edge.a,edge.b):
                uf.union(edge.a,edge.b)
                min_cost += edge.cost
                
                count -= 1

        return min_cost