class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # search_space = 
        left = 0
        right = len(arr)
        
        def checkFeasible(mid):
            if arr[mid] - mid - 1 >= k:
                return True
            else:
                return False
        
        
        while left < right:
            mid = left + (right - left) // 2
            
            if checkFeasible(mid):
                right = mid
            else:
                left = mid + 1
            
        
        return left + k