class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        prev = matrix[0]
        for i in range(1,m):
            curr = []
            for j in range(n):
                leftBound = max(0,j-1)
                rightBound = min(n-1,j + 1)
                curr.append(min(prev[leftBound:rightBound+1]) + matrix[i][j])
            prev = curr.copy()
        
        return min(prev)