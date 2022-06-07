class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        que = deque([])
        que.append((sr,sc))
        
        m = len(image)
        
        n = len(image[0])
        
        targetPixel = image[sr][sc]
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        visited = set()
        visited.add((sr,sc))
        
        while que:
            a,b = que.popleft()
            
            if image[a][b] == targetPixel:
                image[a][b] = newColor
            else:
                continue
            
            for n_r,n_c in directions:
                row = n_r + a
                col = n_c + b
                if row < 0 or row >= m or col < 0 or col >= n or image[row][col] != targetPixel or (row,col) in visited:
                    continue
                que.append((row,col))
                visited.add((row,col))
            
        return image