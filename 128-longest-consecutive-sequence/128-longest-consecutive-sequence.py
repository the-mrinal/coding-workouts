class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        set_nums = set(nums)
        maxLen = 0
        for i in range(n):
            if nums[i] - 1 not in set_nums:
                start = nums[i]
                currLen = 1
                while start + 1 in set_nums:
                    currLen += 1
                    start += 1
                maxLen = max(maxLen,currLen)
        
        return maxLen