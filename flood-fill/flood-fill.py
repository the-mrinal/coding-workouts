class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        m = len(image)
        
        n = len(image[0])
        
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        
        queue = deque([])
        queue.append([sr,sc])
        
        oldPixel = image[sr][sc]
        
        visited = []
    
        while queue:
            r_u,c_u = queue.popleft()
            
            image[r_u][c_u] = newColor
            
            for r_d,c_d in directions:
                r_n = r_u + r_d
                c_n = c_u + c_d
                
                if r_n < 0 or r_n >= m or c_n < 0 or c_n >= n or image[r_n][c_n] != oldPixel or [r_n,c_n] in visited:
                    continue
                
                queue.append([r_n,c_n])
                visited.append([r_n,c_n])
        
        return image