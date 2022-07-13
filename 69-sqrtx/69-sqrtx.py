class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x + 1 if x == 1 else x // 2 + 1
        
        def condition(mid):
            if mid * mid <= x:
                return False
            return True
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left - 1