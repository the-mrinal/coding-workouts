class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = - n
        
        hashMap = {}
        
        def helper(t):
            if t == 0:
                return 1
            if t == 1:
                return x
            
            if t in hashMap:
                return hashMap[t]
            
            middle = t // 2
            other = t - middle
            
            hashMap[t] = helper(middle) * helper(other)
            return hashMap[t]
        
        return helper(n)