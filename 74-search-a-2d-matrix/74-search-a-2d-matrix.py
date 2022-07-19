class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        total = m*n
        
        left = 0
        right = total
        
        def condition(mid):
            row,col = mid // n,mid % n
            if matrix[row][col] >= target:
                return True
            return False
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        row = left // n
        col = left % n
        return True if row < m and col < n and matrix[row][col] == target else False 