class Solution:
    
        # def mySqrt(self,x: int) -> int:
        #     left, right = 0, x
        #     while left < right:
        #         mid = left + (right - left) // 2
        #         if mid * mid <= x:
        #             left = mid + 1
        #         else:
        #             right = mid
        #     return left - 1

    
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        
        def check(mid):
            t = mid * mid
            if t > x:
                return True # ie, go to left search space
            else:
                return False
            
        
        
        left = 2
        right = x
        while left < right:
            mid = left + (right - left) // 2
            
            if check(mid):
                right = mid
            else:
                left = mid + 1
        
        return left - 1