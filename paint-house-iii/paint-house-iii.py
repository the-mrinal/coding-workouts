class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, t: int) -> int:
        dp = {}	

        # (i,t,p) -> where t is the no of neighbourhood from i to m and the ith house is painted with p

        def dfs(i,t,p):
            key = (i,t,p)

            if i == m or t < 0 or m - i < t:
                # if i reached the end or t is negative (ie, we have negative neighbourhood )
                # or the remaining houses is less tthen req neighbourhood then their is no point going forward. we can end it here. helps in pruning dp branches.
                return 0 if i == m and t == 0 else float('inf')


            if key not in dp:
                if houses[i] == 0: # not painited ie, we  have to find the min possible solution to pain the house given we will have t neighbourse from i to m.
                    dp[key] = min(dfs(i+1,t - (nc != p),nc)+ cost[i][nc - 1] for nc in range(1,n + 1))
                else: # house already painted. nothing to do here move aheadd.
                    dp[key] = dfs(i+1,t - (houses[i] != p),houses[i])



            return dp[key]

        # here we are calling sp with 0th house and t neigh and -1 color, so that it will search min from whole color space and -1 is not a index.
        result = dfs(0,t,-1)

        return result if result < float('inf') else - 1
