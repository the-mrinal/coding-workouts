class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        si = 0
        ei = len(nums) - 1
        last = None
        while si <= ei:
            mid = si + (ei - si)//2
            
            if nums[mid] < target:
                si = mid + 1
            elif nums[mid] >= target:
                ei = mid - 1
            
        return si