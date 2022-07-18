class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def helper(left,right):
            currMax = 0
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    currMax += 1
                else:
                    break
                left -= 1
                right += 1
            return currMax
        total = 0
        for i in range(n):
            a = helper(i,i)
            b = helper(i,i+1)
            total += a + b
        return total