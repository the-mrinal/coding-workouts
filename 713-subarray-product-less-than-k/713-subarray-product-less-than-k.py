class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start = 0
        count = 0
        prod = 1
        n = len(nums)
        for end in range(n):
            prod *= nums[end]
            
            while prod >= k and start < end:
                prod = prod / nums[start]
                start += 1
            
            if prod < k:
                count += (end - start + 1)
        
        return count