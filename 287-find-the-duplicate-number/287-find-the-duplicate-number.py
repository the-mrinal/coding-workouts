class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        
        def condition(mid):
            currSum = sum([num <= mid for num in nums])
            
            return currSum > mid
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
            
        
        return left