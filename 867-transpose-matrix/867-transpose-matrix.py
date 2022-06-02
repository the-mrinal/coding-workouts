class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            curr_row = []
            for j in range(m):
                    curr_row.append(matrix[j][i])
            res.append(curr_row)

        return res
