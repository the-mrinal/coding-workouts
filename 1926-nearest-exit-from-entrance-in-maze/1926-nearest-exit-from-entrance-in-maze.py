class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        que = deque([(entrance,0)])
        visited = set()
        visited.add((entrance[0],entrance[1]))
        m = len(maze)
        n = len(maze[0])
        while que:
            curr,step = que.popleft()
                
            for next_x,next_y in [[1,0],[0,1],[-1,0],[0,-1]]:
                new_x = next_x + curr[0]
                new_y = next_y + curr[1]
                
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or maze[new_x][new_y] == '+' or (new_x,new_y) in visited:
                    continue
                if (new_x == 0 or new_x == m-1 or new_y == 0 or new_y == n-1) and maze[new_x][new_y] == '.':
                    return step + 1
                que.append(((new_x,new_y),step+1))
                visited.add((new_x,new_y))
        return -1