class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        1 2 3 1
        dp [ max profit till house i]
        dp[0] = nums[0]
        dp[1] = max(nums[i],nums[i - 1])
        
        dp[3] = max(nums[i] + dp[i - 2] , dp[i - 1])
        
        '''
        n = len(nums)
        dp = [0 for _ in range(n)]
        if n <= 2:
            return max(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2,n):
            dp[i] = max(nums[i] + dp[i - 2],dp[i-1])
        
        return dp[n - 1]