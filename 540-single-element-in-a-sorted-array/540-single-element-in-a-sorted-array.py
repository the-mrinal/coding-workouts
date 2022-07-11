class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        si = 0
        ei = n - 1
        
        
        
        while si < ei:
            mid = si +(ei - si)//2
            even_half = (ei - mid)%2 == 0
            if nums[mid + 1] == nums[mid]:
                if even_half:
                    si = mid + 2
                else:
                    ei = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if even_half:
                    ei = mid - 2
                else:
                    si = mid + 1
            else:
                return nums[mid]
                
        return nums[si]
    
    
    
    
    
    