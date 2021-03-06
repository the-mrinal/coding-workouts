class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums % 2 != 0:
            return False
        return self.KSumSubSeq(nums,sums // 2)
    
    def KSumSubSeq(self,nums,K):
        n = len(nums)
        dp = [[0 for _ in range(K + 1)] for _ in range(2)]
        
        for i in range(K + 1):
            dp[0][i] = True if i == nums[0] else False
        for i in range(1,n):
            for j in range(K+1):
                if nums[i] <= j:
                    dp[i%2][j] = dp[(i - 1)%2][j - nums[i]]
                dp[i%2][j] = dp[i%2][j] or dp[(i - 1)%2][j]
        
        return dp[(n - 1)%2][K]