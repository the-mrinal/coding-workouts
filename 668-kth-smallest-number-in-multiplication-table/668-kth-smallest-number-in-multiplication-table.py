class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left = 1
        right = m * n
        
        def condition(val): # target will be to find count of dgits present that are smaller than given number.
            count = 0
            for num in range(1,m + 1): # traverse rows
                add = min(val // num, n)
                count += add
                if add == 0:
                    break
            return count >= k
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left