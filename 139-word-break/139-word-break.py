class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        '''
        
        #leetcode
        #['leet','code']
        n = len(s)
        dp = [False] * n
        
        
        for i in range(n): # n is len of s
            for word in words:
                if i >= len(word) - 1 and (i == len(word) - 1 or dp[i - len(word)]):
                    if s[i - len(word) + 1:i+1] == word:
                        dp[i] = True
                        break
        
        return dp[n - 1]
        
        
        '''
        
        n = len(s)
        dp = [False] * n
        
        
        for i in range(n): # n is len of s
            for word in words:
                if i >= len(word) - 1 and (i == len(word) - 1 or dp[i - len(word)]):
                    if s[i - len(word) + 1:i+1] == word:
                        dp[i] = True
                        break
        
        return dp[n - 1]