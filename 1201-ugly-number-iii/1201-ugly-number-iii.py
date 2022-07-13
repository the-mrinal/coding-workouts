class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        MOD = 10**9 + 7
        left = min(a,b,c)
        right = 10**10
        
        ab = a*b // math.gcd(a,b)
        ac = a*c // math.gcd(a,c)
        bc = b *c // math.gcd(b,c)
        abc = a * bc // math.gcd(a,bc)
        
        def condition(ugly):
            num =  ugly//a + ugly//b + ugly//c - ugly // ab - ugly // ac - ugly//bc + ugly // abc
            return num >= n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
            
        
        