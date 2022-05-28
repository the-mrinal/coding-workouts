class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        que = deque([])
        
        m = len(mat)
        
        n = len(mat[0])
        
        dist = [[-1 for _ in range(n)]for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    que.append([i,j,0])
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        
        visited = set()
        
        while que:
            r,c,depth = que.popleft()
            
            if (r,c) in visited:
                continue
            
            visited.add((r,c))
            if dist[r][c] == -1:
                dist[r][c] = depth
            
            
            for d_r,d_c in directions:
                n_r = d_r + r
                n_c = d_c + c
                
                if n_r < 0 or n_r  >= m or n_c < 0 or n_c >= n or dist[n_r][n_c] != -1 or (n_r,n_c) in visited:
                    continue
                
                que.append([n_r,n_c,depth + 1])

        
        return dist