class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
	
        m = len(heights)
        n = len(heights[0])

        pacific_side = deque()
        atlantic_side = deque()

        for i in range(m): # all the rows
            pacific_side.append((i,0))
            atlantic_side.append((i,n-1))

        for j in range(n): # all the cols
            pacific_side.append((0,j))
            atlantic_side.append((m-1,j))
            
            
            
        


        def dfs(curr_que):
            que = curr_que
            eligible_set = set()

            while que:
                x,y = que.popleft()
                eligible_set.add((x,y))
                for dx,dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                    nx = dx+x
                    ny = dy + y
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or (nx,ny) in eligible_set:
                        continue
                    if heights[nx][ny] < heights[x][y]:
                        continue
                        
                    que.append([nx,ny])

            return eligible_set



        pacific_set = dfs(pacific_side)
        atlantic_set = dfs(atlantic_side)                                

        return list(pacific_set.intersection(atlantic_set))
