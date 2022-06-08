# self.root = [i for i in range(m *n)]
        
        
#         def find(x):
#             if x == self.root[x]:
#                 return x
#             self.root[x] = self.find(self.root[x])
#             return self.root[x]
        
#         def union(a,b):
#             rootA = self.find(a)
#             rootB = self.find(b)
            
#             if rootA != rootB:
#                 self.root[rootB] = rootA
#                 return False
#             else:
#                 return True
            
#         for 

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        
        maxSoFar = float('-inf')
        def dfs(x,y):
            nonlocal maxSoFar
            st = [(x,y)]
            currMax = 0
            visited = set()
            visited.add((x,y))
            while st:
                c_x,c_y = st.pop()
                currMax += 1
                # print(currMax,c_x,c_y)
                grid[c_x][c_y] = 0
                for n_x,n_y in directions:
                    u_x = n_x + c_x
                    u_y = n_y + c_y
                    
                    if u_x < 0 or u_x >= m or u_y < 0 or u_y >= n or grid[u_x][u_y] == 0 or (u_x,u_y) in visited:
                        continue
                    st.append((u_x,u_y))
                    visited.add((u_x,u_y))
            # print(x,y,currMax,'--')
            maxSoFar = max(currMax,maxSoFar)
            
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
        
        return maxSoFar if maxSoFar > float('-inf') else 0
         
                    
                    
                    
                    
                    