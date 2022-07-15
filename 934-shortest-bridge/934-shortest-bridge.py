class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def findRoot():
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        return (i,j)
            
            return (-1,-1)
        
        def isNotValid(x,y):
            if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] == -1:
                return True
            return False

        root = findRoot()
        stack = [root]
        bound = []

        while stack:
            curr = stack.pop()

            grid[curr[0]][curr[1]] = -1

            for neigh in directions:
                new_x = neigh[0] + curr[0]
                new_y = neigh[1] + curr[1]

                if isNotValid(new_x,new_y):
                    continue

                if grid[new_x][new_y] == 0:
                    bound.append([new_x,new_y])
                else:
                    stack.append((new_x,new_y))

        def findMinRoute():
            nonlocal bound
            step = 1
            while bound:
                new = []
                for i, j in bound:
                    for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                        if 0 <= x < n and 0 <= y < n:
                            if grid[x][y] == 1:
                                return step
                            elif not grid[x][y]:
                                grid[x][y] = -1
                                new.append((x, y))
                step += 1
                bound = new


        return findMinRoute()




