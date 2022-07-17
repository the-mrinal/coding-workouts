class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        def rotate():
            top = 0
            bottom = n - 1
            while top < bottom:
                for col in range(n):
                    mat[top][col],mat[bottom][col] = mat[bottom][col],mat[top][col]
                top += 1
                bottom -= 1
            
            for row in range(n):
                for col in range(n):
                    if row < col:
                        mat[row][col],mat[col][row] = mat[col][row],mat[row][col]
            
        for _ in range(4):
            if mat == target:
                return True
            rotate()
        return False