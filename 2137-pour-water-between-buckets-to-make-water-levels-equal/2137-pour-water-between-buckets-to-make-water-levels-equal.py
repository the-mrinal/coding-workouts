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
            
            # this formual is given in hints i just copy pasted it. 
            if float(out - (out * (loss/100))) >= float(ind):
                return False # going right to maximise the output
            else:
                return True # going left when failing the case
            
        
        left = 0
        right = max(buckets)
        elipsion = 10**-5
        
        
        while right - left > elipsion:
            mid = float(left + (right - left) / 2)

            if isFeasible(mid):
                right = mid
            else:
                left = mid
        
        return left