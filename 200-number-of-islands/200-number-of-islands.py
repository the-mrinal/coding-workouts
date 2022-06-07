class UnionFind:
    def __init__(self,grid):    
        m = len(grid)
        n = len(grid[0])
        self.count = sum(grid[i][j]=='1' for i in range(m) for j in range(n))
        self.root = [i for i in range(m*n)]
        self.rank = [0 for _ in range(m*n)]

    def find(self,x):
        if x == self.root[x]:
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
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        uf = UnionFind(grid)
        directions = [[1,0],[0,1]]
        print(uf.count)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                index = i*n + j
                if j < n-1 and grid[i][j+1] == '1':
                    uf.union(index, index+1)
                if i < m-1 and grid[i+1][j] == '1':
                    uf.union(index, index+n)

        print(uf.count)
        return uf.count