class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxSize = 0
        maxVal = ""
        def findP(left,right):
            nonlocal maxSize,maxVal
            currSize = 0
            while left >= 0 and right < n:
                if left != right and s[left] == s[right]:
                    currSize += 2
                elif s[left] == s[right]:
                    currSize += 1
                else:
                    break
                left -= 1
                right += 1
            if currSize > maxSize:
                maxSize = currSize
                # print(left,,right)
                maxVal = s[left + 1:right]
        
        for i in range(n):
            findP(i,i)
            findP(i,i+1)
        
        return maxVal