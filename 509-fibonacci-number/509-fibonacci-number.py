class Solution:
    def __init__(self):
        self.cache = {}
    
    
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        if n not in self.cache:
            self.cache[n] = self.fib(n-1)+ self.fib(n-2)
        
        return self.cache[n]