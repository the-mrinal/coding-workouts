class Solution:
    def change(self, amount: int, coins: List[int]) -> int:     
        @lru_cache(None)
        def dp(amountLeft,i):
            if amountLeft == amount:
                return 1
            if amountLeft > amount:
                return 0
            if i == len(coins):
                return 0

            soln = dp(amountLeft + coins[i],i) + dp(amountLeft,i+1)
            return soln
        
        return dp(0,0)