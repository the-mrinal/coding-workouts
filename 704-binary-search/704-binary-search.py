class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        si = 0
        ei = len(nums) - 1
        
        while si <= ei:
            mid = si + (ei - si)//2
            
            if nums[mid] < target:
                si = mid + 1
            elif nums[mid] > target:
                ei = mid - 1
            else:
                return mid
        return -1