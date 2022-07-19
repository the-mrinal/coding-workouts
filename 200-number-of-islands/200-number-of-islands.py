class UnionFind:
    
    def __init__(self,grid):
        rowSize = len(grid)
        colSize = len(grid[0])
        self.count = sum([sum([int(grid[i][j]) for j in range(colSize)]) for i in range(rowSize)])
        self.root = [i for i in range(rowSize*colSize)]
        self.rank = [1 for i in range(rowSize * colSize)]
    
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
            elif self.rank[rootB] > self.rank[rootA]:
                self.root[rootA] = rootB
            else:
                self.root[rootB] = rootA
                self.rank[rootA] += 1
            self.count -= 1        


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rowS = len(grid)
        colS = len(grid[0])
        
        uf = UnionFind(grid)
        
        
        for i in range(rowS):
            for j in range(colS):
                index = i *colS + j
                if grid[i][j] == '1':
                    if j < colS - 1 and grid[i][j + 1] == '1':
                        uf.union(index,index + 1)
                    if i < rowS - 1 and grid[i+1][j] == '1':
                        uf.union(index,index + colS)
        return uf.count
        
        
        
        
        
        
        
        
        
        