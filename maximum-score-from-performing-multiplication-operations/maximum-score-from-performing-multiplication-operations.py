# class Solution:
#     def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
#         m = len(multipliers)
#         n = len(nums)
        
#         @lru_cache(2000)
#         def dp(i,left): #<- the index if multiplier, left <- the index of nums we are at
#             if i == m:
#                 return 0 #<- this means we reached the end of flow . 

#             mul = multipliers[i]
#             right = n - 1 - (i - left)
#             # either mul * nums[left] + dp[i+1,left +1] or mul*nums[right] + dp[i+1,left]
#             return  max(mul*nums[left] + dp(i+1,left + 1),mul* nums[right] + dp(i+1,left))
        
#         return dp(0,0)


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        dp = [[0]*(m+1) for _ in range(m+1)]

        for i in range(m-1,-1,-1):
            for left in range(i,-1,-1):
                mul = multipliers[i]
                right = n - 1 - (i - left)
                a = mul * nums[left] + dp[i + 1][left + 1]
                b = mul * nums[right] + dp[i+1][left]
                dp[i][left] = max(a,b)

        return dp[0][0]
