class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def condition(mid):
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return True
            return False
        
        left = 0
        right = len(nums)
        
        while left < right:
            mid = left + (right - left)//2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
            
        
        return left - 1