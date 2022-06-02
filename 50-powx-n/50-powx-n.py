class Solution:
    def myPow(self, base: float, val: int) -> float:
        cache = {}
        def power(x,n):
            if n == 1:
                return x
            if n == 0:
                return 1

            if n in cache:
                return cache[n]

            mid = n // 2

            otherMid = n - mid

            res = float(power(x,mid) * power(x,otherMid))

            cache[n] = res
            return res
        
        
        if val < 0:
            val = - val
            base = 1/base
        
        return power(base,val)
