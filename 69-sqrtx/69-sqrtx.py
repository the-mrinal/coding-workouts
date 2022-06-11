class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        
        
        def isFeasible(mid):
            if mid * mid > x:
                return True
            return False
        
        left = 2
        right = x 
        
        while left < right:
            mid = left + (right - left) // 2
            
            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1
            
        return left - 1