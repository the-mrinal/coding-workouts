class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bsearch(left,right):
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1
    
        n = len(nums)
        
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1
        
        index = 1
        while index < n and nums[index] > nums[index -1]:
            index += 1
        
        if target >= nums[0]:
            return bsearch(0,index - 1)
        else:
            return bsearch(index,n - 1)

        
        