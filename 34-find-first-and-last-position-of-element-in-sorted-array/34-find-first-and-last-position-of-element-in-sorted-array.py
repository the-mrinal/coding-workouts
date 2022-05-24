class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        
        def feasibleFindStart(mid):
            if nums[mid] <= target:
                if nums[mid] == target:
                    if mid != 0 and nums[mid - 1] == nums[mid]:
                        return True
                    return False
                return False
            return True
        
        def feasibleFindEnd(mid):
            if nums[mid] <= target:
                if nums[mid] == target:
                    if mid != len(nums)-1 and nums[mid + 1] == nums[mid]:
                        return False
                    return True
                return False
            return True
        
        left = 0
        
        right = len(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if feasibleFindStart(mid):
                right = mid
            else:
                left = mid + 1
        
        print(left -1 )
        if nums[left - 1] == target:
            si = left - 1
            left = si
            right = len(nums)
            
            while left < right:
                mid = left + (right - left)//2
                if feasibleFindEnd(mid):
                    right = mid
                else:
                    left = mid + 1
            ei = left
            print(ei)
            return [si,ei]
        return [-1,-1]
        
        