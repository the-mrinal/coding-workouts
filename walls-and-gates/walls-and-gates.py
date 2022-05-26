class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        MAX_VAL = 2**30
        queue = deque([])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        
        m = len(rooms)
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append([i,j])
        
        while queue:
            row,col = queue.popleft()
            
            for a,b in directions:
                r = row + a
                c = col + b
                if (r < 0 or r >= m or c < 0 or c >= n or rooms[r][c] <  MAX_VAL):
                    continue
                rooms[r][c] = rooms[row][col] + 1
                
                queue.append([r,c])
