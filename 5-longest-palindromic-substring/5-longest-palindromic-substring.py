class Solution:
    def longestPalindrome(self, s: str) -> str:
        # babad
        st = 0
        maxLen = 0
        n = len(s)
        def findMax(start,end):
            nonlocal maxLen,st,n
            while start > -1 and end < n and s[start] == s[end]:
                start -= 1
                end += 1
            if maxLen < end - start - 1:
                maxLen = end- start - 1
                st = start + 1
    
        
        for i in range(n):
            findMax(i,i)
            findMax(i,i+1)

        return s[st:st+maxLen]
