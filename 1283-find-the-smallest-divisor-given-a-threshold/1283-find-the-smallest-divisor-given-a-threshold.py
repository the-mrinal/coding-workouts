class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        
        def condition(divisor):
            total = 0
            for num in nums:
                total += math.ceil(num / divisor) 
                if total > threshold:
                    return False
            return True
        
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left