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
            return False
        
        if self.rank[rootA] > self.rank[rootB]:
            self.root[rootB] = rootA
        elif self.rank[rootA] < self.rank[rootB]:
            self.root[rootA] = rootB
        else:
            self.root[rootB] = rootA
            self.rank[rootA] += 1
        
        self.count -= 1
        
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        
        for a,b in edges:
            if not uf.union(a,b):
                return False
            
        if uf.count > 1:
            return False
        return True