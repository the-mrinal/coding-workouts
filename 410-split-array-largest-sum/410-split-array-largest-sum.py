class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)
        
        def condition(currSum):
            localSum,count = 0,1
            for num in nums:
                localSum += num
                
                if localSum > currSum:
                    localSum = num
                    count += 1
                
                if count > m:
                    return False
            return True
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
            
        return left