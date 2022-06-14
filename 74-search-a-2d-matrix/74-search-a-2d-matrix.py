class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        total = m * n
        
        # n*col + row -> [row][col]
        # given x -> x / col <- curr_col and x&col <- curr_row
        
        si = 0
        ei = total
        
        def isFeasible(mid):
            col ,row = mid % n , mid // n
            if matrix[row][col] >= target:
                return True
            return False
        
        
        while si < ei:
            mid = si + (ei - si)//2
            
            if isFeasible(mid):
                ei = mid
            else:
                si = mid + 1
        
        
        col ,row = si % n , si // n
        return True if row < m and col < n and matrix[row][col] == target else False
        
        