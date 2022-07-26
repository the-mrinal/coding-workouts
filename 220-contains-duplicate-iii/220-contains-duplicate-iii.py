class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # bucket sort
        
        n = len(nums)
        cache = {}
        w = t + 1
        for i in range(n):
            cache_index = nums[i] // w
            
            if cache_index in cache:
                return True
            if cache_index - 1 in cache and abs(nums[i] - cache[cache_index - 1]) < w:
                return True
            if cache_index + 1 in cache and abs(nums[i] - cache[cache_index + 1]) < w:
                return True
            
            cache[cache_index] = nums[i]
            if i >= k: del cache[nums[i - k] // w]
        
        return False
            