class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        que = deque([(i,j) for i in range(n) for j in range(n) if grid[i][j] == 1])
        
        if len(que) == n*n or len(que) == 0: return -1
        
        level = 0
        
        while que:
            size = len(que)
            
            for _ in range(size):
                x,y = que.popleft()
                
                for n_x,n_y in [[1,0],[0,1],[-1,0],[0,-1]]:
                    u_x = n_x + x
                    u_y = n_y + y
                    
                    if u_x >=0 and u_x < n and u_y >= 0 and u_y < n and grid[u_x][u_y] == 0:
                        que.append((u_x,u_y))
                        grid[u_x][u_y] = 1
                
            level += 1
        
        return level - 1