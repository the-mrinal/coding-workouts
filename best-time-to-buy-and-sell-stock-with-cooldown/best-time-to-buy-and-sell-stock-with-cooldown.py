class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}
        def dfs(i,isHolding,isCooling):
            if i == n:
                return 0
            key = (i,isHolding,isCooling)
            if key not in dp:
                dp[key] = 0
                doNothing = dfs(i+1,isHolding,False)
                doSomething = 0
                if isHolding:
                    doSomething = prices[i] + dfs(i+1,False,True)
                if not isHolding and not isCooling:
                    doSomething = -prices[i] + dfs(i+1,True,False)

                dp[key] = max(doNothing,doSomething)
            
            return dp[key]
            
            
        return dfs(0,False,False)