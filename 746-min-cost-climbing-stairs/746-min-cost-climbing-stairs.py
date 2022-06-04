# def dp(i):
# 	if i == 0:
# 		return cost[0]
# 	if i <= 2:
# 		return min(cost[i],cost[i-1])


# 	moeny = min(dp(i-1),dp(i-2))



class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return cost[0]
        if n < 3:
            return min(cost[0],cost[1])        
        
        def dp(i):
            if i <= 1:
                return 0
            
            if i not in memo:
                memo[i] = min(dp(i-1)+cost[i-1] , dp(i-2) + cost[i-2])
            
            return memo[i]
        
        memo = {}
        return dp(n)
        