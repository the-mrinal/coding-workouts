
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        
        self.root = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.count = n
        def find(x):
            if x == self.root[x]:
                return x
            self.root[x] = find(self.root[x])
            return self.root[x]
        
        def union(a,b):
            rootA = find(a)
            rootB = find(b)
            
            if rootA != rootB:
                if self.rank[rootA] < self.rank[rootB]:
                    self.root[rootA] = rootB
                elif self.rank[rootA] > self.rank[rootB]:
                    self.root[rootB] = rootA
                else:
                    self.root[rootB] = rootA
                    self.rank[rootA] += 1
                self.count = self.count - 1
                    
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    union(i,j)
                    
        return self.count