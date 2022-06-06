# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         @lru_cache(None)
#         def	dp(i):
#             nonlocal max_sum
#             if i == 0:
#                 max_sum = max(max_sum,1)
#                 return 1
#             if i == 1:
#                 ans = 2 if nums[0] < nums[1] else 1
#                 max_sum = max(max_sum,ans)
#                 return ans

#             res = 1
#             non_res = 0
#             for k in range(i):
#                 if nums[k] < nums[i]:
#                     res = max(res,dp(k) + 1)
#                 else:
#                     non_res = max(non_res,dp(k))
#             max_sum = max(max_sum,max(non_res,res))
#             return res
#         max_sum = float('-inf')
#         dp(len(nums) - 1)
        
#         return max_sum


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [1 for _ in range(n)]
        
        for i in range(n):        
            for k in range(i):
                if nums[i] > nums[k]:
                    dp[i] = max(dp[i],dp[k] + 1)
                    
        return max(dp)
        
        
        
        
        
        
        
        