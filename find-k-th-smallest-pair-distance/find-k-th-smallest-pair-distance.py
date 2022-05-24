class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def isFeasible(guess):
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k
        
        nums.sort()
        
        left = 0
        right = abs(nums[0] - nums[-1])
        
        while left < right:
            mid = left + (right - left) // 2
            
            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1
        

        return left