class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1 for _ in range(n)]
        
        for i in range(0,n - 1):
            result[i + 1] = nums[i] * result[i]
            
        r = nums[-1]
        for j in range(n - 1,0,-1):
            result[j - 1] =result[j - 1] * r
            r = r * nums[j - 1]
        return result