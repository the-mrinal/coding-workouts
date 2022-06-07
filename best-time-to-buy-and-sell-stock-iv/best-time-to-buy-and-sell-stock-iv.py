class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dp(i,transactionLeft,isHolding):
            if i == n or transactionLeft == 0:
                return 0

            money = 0
            if isHolding:
                money = max(dp(i+1,transactionLeft,isHolding),prices[i] + dp(i+1,transactionLeft - 1,False))
            else:
                money = max(dp(i+1,transactionLeft,isHolding),-prices[i] + dp(i+1,transactionLeft,True))

            return money

        return dp(0,k,False)