class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # longest sub arr that sums up to total - x
        # that will result in min subarr that will give us x
        
        target = sum(nums) - x
        maxLen = -1
        currSum = 0
        start = 0
        n = len(nums)
        for end in range(n):
            currSum += nums[end]
            
            while currSum > target and start <= end:
                currSum -= nums[start]
                start += 1
            
            if currSum == target:
                maxLen = max(maxLen,end - start + 1)
        
        return n - maxLen if maxLen != -1 else -1