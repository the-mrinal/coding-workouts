class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        que = deque()
        
        
        def findRoot():
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        que.append([i,j,0,[(i,j)]])
                        
        findRoot()
        
        while que:
            x,y,index,indexReq = que.pop()
            
            if index == len(word) - 1:
                return True
            
            
            for neigh in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_x = neigh[0] + x
                new_y = neigh[1] + y
                
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or board[new_x][new_y] != word[index + 1] or (new_x,new_y) in indexReq:
                    continue
                que.append([new_x,new_y,index + 1,indexReq + [(new_x,new_y)]])
        return False