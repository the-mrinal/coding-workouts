class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        def isFeasible(i):
            if arr[i] <= arr[i+1]:
                return False
            else:
                return True
        
        
        si = 1
        ei = len(arr) - 1
        
        if ei < 2:
            return -1
        
        while si < ei:
            mid = si + (ei - si)//2
            if isFeasible(mid):
                ei = mid
            else:
                si = mid + 1
            
        return si