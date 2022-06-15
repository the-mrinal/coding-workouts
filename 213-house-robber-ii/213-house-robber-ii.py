class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        def simple(arr):
            prev = 0
            curr = 0
            for i in arr:
                temp = curr
                curr = max(i+prev,curr)
                prev = temp
            
            return curr
        
        return max(simple(nums[1:]),simple(nums[:-1]))
    
