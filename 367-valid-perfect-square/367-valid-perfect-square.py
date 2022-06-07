class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        
        def isFeasible(n):
            if n*n < num:
                return False
            else:
                return True
        
        left = 2
        right = num // 2
        
        while left < right:
            mid = left + (right - left)//2
            
            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return True if left * left == num else False