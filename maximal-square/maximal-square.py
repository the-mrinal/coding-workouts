class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        maxSoFar = 0
        for i in range(n):
            maxSoFar = max(maxSoFar,int(matrix[0][i]))
        for j in range(m):
            maxSoFar = max(maxSoFar,int(matrix[j][0]))
        
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == '1':
                    matrix[i][j] = min(int(matrix[i-1][j]),int(matrix[i][j-1]),int(matrix[i-1][j-1])) + 1
                    print(matrix[i][j])
                    maxSoFar = max(maxSoFar,matrix[i][j])

        return maxSoFar*maxSoFar
