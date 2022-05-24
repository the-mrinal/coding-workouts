class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # for just finding the left bound since we have to find k closed , so ei = len(arr) - k
        
        def isFeasible(mid):
            return x - arr[mid] > arr[mid +k] - x
        
        si = 0
        ei = len(arr) - k
        
        while si < ei:
            mid = (si + ei) // 2
            if isFeasible(mid):
                si = mid + 1
            else:
                ei = mid
            
        return arr[si:si + k]
        
        