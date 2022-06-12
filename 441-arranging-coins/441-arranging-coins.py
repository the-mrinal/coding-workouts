class Solution:
    def arrangeCoins(self, n: int) -> int:

        # sums = 0
        # for i in range(n + 1):
        #     sums += i
        #     if sums == n:
        #         return i
        #     elif sums > n:
        #         return i - 1
        si = 0
        ei = n
        
        
        def isFeasible(mid):
            
            t = int(mid*(mid+1)/2)
            if t < n:
                return False
            else:
                return True
        
        while si < ei:
            mid = si + (ei - si)//2
            
            if isFeasible(mid):
                ei = mid
            else:
                si = mid + 1
            
        return si if int(si*(si+1)/2) == n else si - 1