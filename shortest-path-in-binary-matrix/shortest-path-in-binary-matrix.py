class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1:
            return -1
        directions = [[0,1],[1,0],[0,-1],[-1,0],[-1,-1],[1,1],[-1,1],[1,-1]]
        que = deque([[0,0,1]])
        visited = set((0,0))
        while que:
            a,b,cost = que.popleft()
            if a == n-1 and b == n-1:
                return cost 

    
            for n_a,n_b in directions:
                x = a + n_a
                y = b + n_b

                if x >= 0 and x < n and y >= 0 and y < n and grid[x][y] == 0 and (x,y) not in visited:
                        que.append([x,y,cost + 1])
                        visited.add((x,y))



        return -1
