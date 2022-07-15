class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        new_s = s

        def helper(left,right):
            ans = 0 
            while left > -1 and right < n and new_s[left] == new_s[right]:
                ans = ans + 1
                left -= 1
                right += 1
            return ans
                    
        
        for i in range(n):
            a = helper(i,i)
            b = helper(i,i +1)
            count += a + b
        return count