class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1 for _ in range(2)] for _ in range(n)]
        
        maxVal = 1
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i][0] < dp[j][0] + 1:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    elif dp[i][0] == dp[j][0] + 1:
                        dp[i][1] = dp[i][1]+dp[j][1]
                maxVal = max(maxVal,dp[i][0])
                
        ans = 0
        for length,count in dp:
            if length == maxVal:
                ans += count
        return ans