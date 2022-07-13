class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        left = 0
        right = max(nums) - min(nums)
        n = len(nums)
        nums.sort()
        # 1 3 7 8  10 18 23 24 78
        def condition(distance):
            count, i, j = 0, 0, 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= distance:  # move fast pointer
                    j += 1
                count += j - i - 1  # count pairs
                i += 1  # move slow pointer
            return count >= k

        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
            
                    