class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubArraySum = currSubArraySum = nums[0]
        n = len(nums)
        for i in range(1,n):
            currSubArraySum = max(nums[i],currSubArraySum + nums[i])
            maxSubArraySum = max(maxSubArraySum,currSubArraySum)
        
        return maxSubArraySum