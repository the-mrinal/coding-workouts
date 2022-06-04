class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def create_board(state):
            ans = []
            for row in state:
                ans.append(''.join(row))

            return ans



        def backtrack(row,cols,diagonals,antidiagonals,state):
            if row == n:
                result.append(create_board(state))
                return
            
            for col in range(n):
                diag = row - col
                antidiag = row + col

                if col in cols or diag in diagonals or antidiag in antidiagonals:
                    continue

                cols.add(col)
                diagonals.add(diag)
                antidiagonals.add(antidiag)
                state[row][col] = 'Q'

                backtrack(row + 1,cols,diagonals,antidiagonals,state)


                cols.remove(col)
                diagonals.remove(diag)
                antidiagonals.remove(antidiag)
                state[row][col] = '.'

        state = []
        for i in range(n):
            state.append([])
            for j in range(n):
                 state[-1].append('.')	


        backtrack(0,set(),set(),set(),state)

        return result
