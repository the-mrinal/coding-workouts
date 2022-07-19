class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        currSum = 0
        n = len(nums)
        minLen = float('inf')
        for end in range(n):
            currSum += nums[end]
            
            while currSum >= target and start <= end:
                currSum -= nums[start]
                minLen = min(minLen,end - start + 1)
                start += 1

        
        return minLen if minLen < float('inf') else 0
            