class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        dp = [[]]
        
        for i in range(n):
            size = len(dp)
            for j in range(size):
                curr = dp[j]
                dp.append(curr + [nums[i]])
        return dp
            