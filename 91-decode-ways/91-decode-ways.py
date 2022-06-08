class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(None)
        def dp(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            
            res = dp(i+1)
            if i+1 < n and (int(s[i]) == 1 or int(s[i]) <= 2 and int(s[i + 1]) < 7) :
                print(s[i],int(s[i]) <= 2)
                res += dp(i + 2)
            return res
        return dp(0)
#     def numDecodings(self, s: str) -> int:
#         @lru_cache(None)
#         def dp(i):
#             if i == len(s): return 1
#             ans = 0
#             if s[i] != '0':  # Single digit
#                 ans += dp(i + 1)
#             if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] <= '6'):  # Two digits
#                 ans += dp(i + 2)
#             return ans

#         return dp(0)