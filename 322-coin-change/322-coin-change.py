class Solution:
    def coinChange(self, nums: List[int], amount: int) -> int:

        n = len(nums)
#         cache = {}
#         def dp(index,target):
#             if (index >= n and target != amount) or target > amount:
#                 return float('inf')
#             if target == amount:
#                 cache[(index,target)] = 0
#                 return cache[(index,target)]
#             key = (index,target)
#             if key not in cache:
#                 countA = 1 + dp(index,target+ nums[index])
#                 countB = dp(index+1,target)
#                 cache[key] = min(countA,countB)

#             return cache[key]
#         dp(0,0)
#         return cache[(0,0)] if cache[0,0] < float('inf') else -1
    
        
        dp = [float('inf') for _ in range(amount + 1)]
        
        dp[0] = 0
        
        for coin in nums:
            for j in range(coin,amount + 1):
                dp[j] = min(dp[j],dp[j - coin] + 1)
        
        return dp[amount] if dp[amount] < float('inf') else -1 
        
        