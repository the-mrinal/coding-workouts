class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
    
    def find(self,x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    
    
    def union(self,a,b):
        rootA = self.find(a)
        rootB = self.find(b)
        
        if rootA == rootB:
            return False
        else:
            if self.rank[rootA] > self.rank[rootB]:
                self.root[rootB] = rootA
            
            elif self.rank[rootA] < self.rank[rootB]:
                self.root[rootA] = rootB
            else:
                self.root[rootB] = rootA
                self.rank[rootA] += 1
            
            return True
    def isConnected(self,x,y):
        return self.find(x) == self.find(y)

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
        
        if not points or len(points) == 0:
            return 0
        
        def costF(a,b):
            xi,yi = points[a]
            xj,yj = points[b]
            t = abs(xi - xj) + abs(yi - yj)
            return t
        
        res = []
        for i in range(n-1):
            for j in range(1,n):
                res.append(Edge(i,j,costF(i,j)))
        
        heapq.heapify(res)
        
        
        uf = UnionFind(n)
        
        minCost = 0
        
        count = n -1
        
        while res and count >  0:
            edge = heapq.heappop(res)
            p1 = edge.p1
            p2 = edge.p2
            cost = edge.cost
            if not uf.union(p1,p2):
                continue
            
            count -= 1
            minCost += cost

        
        return minCost
            
            
        
        
        
        
        