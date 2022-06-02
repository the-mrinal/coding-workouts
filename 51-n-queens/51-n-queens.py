class Solution:
    def __init__(self):
	    self.dict = []
    def solveNQueens(self, n: int) -> List[List[str]]:
        def create_board(state):
            ans = []
            for i in state:
                ans.append("".join(i))
            return ans

        def helper(row,diagonals,antidiagonals,cols,state):
            if row == n:
                return self.dict.append(create_board(state))
            soln = []
            for col in range(n):
                diag = row - col
                antidiag = col + row

                if col in cols or diag in diagonals or antidiag in antidiagonals:
                    continue

                cols.add(col)
                diagonals.add(diag)
                antidiagonals.add(antidiag)
                state[row][col] = 'Q'

                helper(row + 1,diagonals,antidiagonals,cols,state)

                cols.remove(col)
                diagonals.remove(diag)
                antidiagonals.remove(antidiag)
                state[row][col] = '.'
        
        state = []
        for i in range(n):
            state.append([])
            for j in range(n):
                state[-1].append('.')

        helper(0,set(),set(),set(),state)
        return self.dict

    
	


		
		