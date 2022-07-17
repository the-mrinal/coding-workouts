class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxSubArrayProd = currSubArrayProd = minSubArrayProd = nums[0]
        n = len(nums)
        for i in range(1,n):
            temp = max(nums[i],currSubArrayProd*nums[i],minSubArrayProd*nums[i])
            minSubArrayProd = min(nums[i],currSubArrayProd*nums[i],minSubArrayProd*nums[i])
            currSubArrayProd = temp
            
            maxSubArrayProd = max(maxSubArrayProd,currSubArrayProd)
        
        return maxSubArrayProd