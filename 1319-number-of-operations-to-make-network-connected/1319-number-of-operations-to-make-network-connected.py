class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        self.count = size
        
        
    def find(self,x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,a,b):
        rootA = self.find(a)
        rootB = self.find(b)
        
        if rootA != rootB:
            if self.rank[rootA] > self.rank[rootB]:
                self.root[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.root[rootA] = rootB
            else:
                self.root[rootB] = rootA
                self.rank[rootA] += 1
            self.count -= 1

    
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        m = len(connections)
        
        if n - 1 > m:
            return -1
        uf = UnionFind(n)
        
        for i in range(m):
            uf.union(connections[i][0],connections[i][1])
        
        return uf.count - 1