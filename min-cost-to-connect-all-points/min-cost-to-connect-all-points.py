class UnionFind:
    
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
    
    
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
        
        if rootA != rootB:
            if self.rank[rootA] > self.rank[rootB]:
                self.root[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.root[rootA] = rootB
            else:
                self.root[rootB] = rootA
                self.rank[rootA] += 1
        return True
    
    def isConnected(self,a,b):
        return self.find(a) == self.find(b)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        listEdge = []
        
        def cost(a,b):
            xi,yi = points[a]
            xj,yj = points[b]
            
            return abs(xi - xj) + abs(yi - yj)
        
        n = len(points)
        
        uf = UnionFind(n)
        
        for i in range(n - 1):
            for j in range(i+1,n):
                listEdge.append([i,j,cost(i,j)])
                
        
        listEdge.sort(key = lambda x:x[2])
        
        minCost = 0
        for a,b,cost in listEdge:
            if not uf.union(a,b):
                continue
            minCost += cost
        
        return minCost
        
        
        
        
        