class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        left = 0
        right = max(nums) - min(nums)
        n = len(nums)
        nums.sort()
        # 1 3 7 8  10 18 23 24 78
        def condition(absDiff):
            count = 0
            i,j = 0,0
            while i < n or j < n:
                while j < n and abs(nums[i] - nums[j]) <= absDiff:
                    j += 1
                count += (j - i - 1)
                i += 1
            return count >= k 
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
            
                    