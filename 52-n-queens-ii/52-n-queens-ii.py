class Solution:
    def totalNQueens(self, n: int) -> int:
      
        def nqueenHelper(row,diag,anti,cols):
            if row == n:
                return 1

            soln = 0
            for col in range(n):
                d = row - col
                ad = row + col

                if col in cols or d in diag or ad in anti:
                    continue

                cols.add(col)
                diag.add(d)
                anti.add(ad)

                soln += nqueenHelper(row + 1,diag,anti,cols)

                cols.remove(col)
                diag.remove(d)
                anti.remove(ad)
            
            return soln

        
        return nqueenHelper(0,set(),set(),set())
