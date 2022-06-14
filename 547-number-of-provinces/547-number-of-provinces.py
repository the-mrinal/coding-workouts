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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        uf = UnionFind(m)
        
        for i in range(m):
            for j in range(m):
                if i!= j and  isConnected[i][j] == 1:
                    uf.union(i,j)
        
        return uf.count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        