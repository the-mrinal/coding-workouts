class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def could_place(row,col,d):
            return not(d in rows[row] or d in cols[col] or d in boxes[box_index(row,col)])
        
        def place_numbers(d,row,col):
            
            
            rows[row][d] += 1
            cols[col][d] += 1
            boxes[box_index(row,col)][d] += 1
            board[row][col] = str(d)
        
        def remove_numbers(d,row,col):
            
            
            del rows[row][d]
            del cols[col][d]
            del boxes[box_index(row,col)][d]
            board[row][col] = '.'
        
        def place_next_numbers(row,col):
            # grid = box_index(row,col)
            
            if col == N-1 and row == N -1:
                nonlocal sudoku_solved
                sudoku_solved = True
            else:
                if col ==  N -1:
                    backtrack(row+1,0)
                else:
                    backtrack(row,col + 1)
        
        
        def backtrack(row = 0,col = 0):
            if board[row][col] == '.':
                    for d in range(1,10):
                        if could_place(row,col,d):
                                place_numbers(d,row,col)
                                place_next_numbers(row,col)
                                if not sudoku_solved:
                                    remove_numbers(d,row,col)
            else:
                place_next_numbers(row,col)
        
        
        n = 3
        
        N = n*n
        
        
        box_index = lambda row,col: (row//n)*n + col // n
        
        rows = [defaultdict(int) for i in range(N)]
        
        cols = [defaultdict(int) for i in range(N)]
        
        boxes = [defaultdict(int) for i in range(N)]        
        
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    place_numbers(int(board[i][j]),i,j)
                    
        sudoku_solved = False
        backtrack()
        