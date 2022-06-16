class Solution:
    def longestPalindrome(self, s: str) -> str:		
        n = len(s)
        st= 0
        max_len = 0
        def expandCenter(si,ei):
            nonlocal max_len,st
            while si > -1 and ei <  n and s[si] == s[ei]:
                si -= 1
                ei += 1
            if max_len < ei - si -1:
                max_len = ei - si - 1
                st = si + 1
    
        
        for start in range(n):
            expandCenter(start,start)
            expandCenter(start,start+1)
        
        
        
        # print()
        return s[st:st + max_len]