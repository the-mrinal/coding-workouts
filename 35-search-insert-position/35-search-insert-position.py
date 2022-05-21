class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
        def check(mid):
            if nums[mid] >= target:
                return True
            else:
                return False
        
        
        left = 0
        right = len(nums)
        
        
        while left < right:
            mid = left + (right - left)//2
            
            if check(mid):
                right = mid
            else:
                left = mid + 1
        
        return left