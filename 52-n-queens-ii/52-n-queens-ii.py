class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def backtrack(row,cols,diagonals,antidiagonals):
            if row == n:
                return 1
            soln = 0
            for col in range(n):
                diag = row - col
                antidiag = row + col
                
                if col in cols or diag in diagonals or antidiag in antidiagonals:
                    continue
                
                cols.add(col)
                antidiagonals.add(antidiag)
                diagonals.add(diag)
                soln += backtrack(row + 1,cols,diagonals,antidiagonals)
                
                cols.remove(col)
                antidiagonals.remove(antidiag)
                diagonals.remove(diag)
                print(soln)
            return soln
    
        return backtrack(0,set(),set(),set())