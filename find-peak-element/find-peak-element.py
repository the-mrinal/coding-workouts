class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        
        
        def isfeasible(mid):
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return True
            else:
                return False
        
        left = 0
        right = len(nums)
        
        while left < right:
            mid = left + (right - left)//2
            
            if isfeasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left - 1