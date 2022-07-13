class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        def condition(currW):
            loaded,daysTaken = 0,1
            for weight in weights:
                loaded += weight
                
                if loaded > currW:
                    daysTaken += 1
                    loaded = weight
                
                if daysTaken > days:
                    return False
            
            return True
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left