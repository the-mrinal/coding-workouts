class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        buckets.sort()

            
        def isFeasible(x):
            out ,ind = 0,0
            for i in buckets:
                if i > x:
                    temp = i - x
                    out += temp
                else:
                    temp = x - i
                    ind += temp
            
            
            if float(out - float(out * float(loss/100))) >= float(ind):
                return False
            else:
                return True
            
        
        left = 0
        right = max(buckets)
        elipsion = 10**-5
        
        
        while right - left > elipsion:
            mid = float(left + float((right - left) / 2))

            if isFeasible(mid):
                right = mid
            else:
                left = mid
        
        return left