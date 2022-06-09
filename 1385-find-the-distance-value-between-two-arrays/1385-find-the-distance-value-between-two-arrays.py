class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        
        m = len(arr1)
        
        n = len(arr2)
        
        def isFeasible(mid,k):
            count = 0

            if k - arr2[mid] > d:
                return True
            else:
                return False
        
        def bSearch(k):
            res = 0
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2
                if abs(k - arr2[mid]) <= d:
                    res += 1
                    break
                elif k < arr2[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return res
        
        # 7 - 2 <= 5
        # 7 - 5 <= 2
        count = 0
        for i in range(m):
            if bSearch(arr1[i]) > 0:
                count += 1
                
        return m - count if count > 0 else 0