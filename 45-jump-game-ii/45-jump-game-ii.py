class Solution:
    def jump(self, nums: List[int]) -> int:
        A, n = nums, len(nums)
        jumps, end, farthest = 0, 0, 0, # The current end and current farthest 
        for i in range(n-1):
            farthest = max(farthest, i+A[i])
            # if farthest >= n-1:
            #     return jumps
            if i == end:
                jumps += 1
                end = farthest
        return jumps