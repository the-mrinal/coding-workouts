#         def dp(index of house):
# 	if index == 1:
# 		return house[i]

# 	if index == 2:
# 		return max(houese1 and house2)
	
# 	money = max(dp(i-1),dp(i-2) + this house)
# 	return money

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        
        
        def dp(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[0],nums[1])
            
            
            if i not in memo:
                memo[i] = max(dp(i-1),dp(i-2)+nums[i])
            
            return memo[i]
        
        memo = {}
        dp(n - 1)
        
        return memo[n- 1]