class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        n = len(nums)
        
        if n == 1:
            return True if nums[0] == target else False
         
        def isFeasible(mid,left,right):
            
            if nums[mid]==target:
                return True

            #step 3
            elif nums[left]<=nums[mid]:
                if nums[mid]>=target and nums[left]<=target:
                    return False
                else:
                    return True

            # step 4
            else:
                if target>=nums[mid] and target<=nums[right]:
                    return True
                else:
                    return False

            

        
        left = 0
        right = n - 1
        
        while left <= right:
            
            
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
                
            
            mid = left + (right - left)//2
                      #step 2
            if nums[mid]==target:
                return True

            #step 3
            elif nums[left]<=nums[mid]:
                if nums[mid]>=target and nums[left]<=target:
                    right=mid-1
                else:
                    left=mid+1

            # step 4
            else:
                if target>=nums[mid] and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        
        return False
            