class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        dp(index):
            if index >= n:
                return 0
            if s[index] == 0:
                return 0
            if index == n - 1:
                return 1
            
            countA = dp(index + 1)
            countB = 0
            if int(s[index: index + 2]) < 27:
                countB = dp(index + 2)
            
            return countA + countB
        
        '''
        n = len(s)
        @lru_cache(None)
        def dp(index):
            if index == n:
                return 1
            if s[index] == "0":
                return 0
            if index == n - 1:
                return 1

            countA = dp(index + 1)
            if int(s[index: index + 2]) < 27:
                countA +=  dp(index + 2)

            return countA
        
        return dp(0)