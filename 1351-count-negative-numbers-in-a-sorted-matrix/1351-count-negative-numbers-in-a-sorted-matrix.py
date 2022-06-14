class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def isFeasible(row,mid):
            if grid[row][mid] < 0:
                return True
            return False
        
        def bSearch(row,si,ei):
            while si < ei:
                mid = si + (ei - si)//2
                if isFeasible(row,mid):
                    ei = mid
                else:
                    si = mid + 1
            return si - 1
        
        
        
        si = 0
        ei = n
        count = 0
        for i in range(m):
            num = bSearch(i,si,ei)
            # print(num,'-')
            if grid[i][num] >= 0 or (num < 0):
                num = num + 1
            count += n - num
            ei = num
        return count