class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isFeasible(cap):
            total = 0
            d = 1
            for w in weights:
                total += w
                if total > cap:
                    total = w
                    d += 1
                    if d > days:
                        return False
            return True

        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = left + (right - left)//2
            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
        
        
  
			
			