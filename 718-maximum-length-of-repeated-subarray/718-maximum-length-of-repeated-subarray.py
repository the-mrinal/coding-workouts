class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        
        n = len(nums2)
        
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m +1)]
        
        maxSoFar = 0
        for i in range(m - 1,-1,-1):
            for j in range(n-1,-1,-1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    maxSoFar = max(maxSoFar,dp[i][j])
        
        return maxSoFar