class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
    
        @lru_cache(None)
        def dp(amountLeft,i):
            if amountLeft == 0:
                return 1
            if amountLeft < 0 or i == len(coins):
                return 0

            return dp(amountLeft - coins[i],i) + dp(amountLeft,i+1)
    
        return dp(amount,0)