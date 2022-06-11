class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        n = len(nums)
        if n == 0:
            return [-1,-1]
        def isFeasible(mid):
            if nums[mid] >= target:
                return True
            return False
        
        def isFeasibleRight(mid):
            if nums[mid] > target:
                return True
            return False
        
        
        def bSearch(si,ei):
            while si < ei:
                mid = si + (ei - si)//2         
                if isFeasible(mid):
                    ei = mid
                else:
                    si = mid + 1
            return si
        
        def bSearchRight(si,ei):
            while si < ei:
                mid = si + (ei - si)//2         
                if isFeasibleRight(mid):
                    ei = mid
                else:
                    si = mid + 1
            return si - 1
        
        
        
        left = bSearch(0,n-1)
        if nums[left] != target:
            return [-1,-1]
        
        right = left
        while right < n and nums[right] == target:
            right += 1
        return [left,right - 1]
        