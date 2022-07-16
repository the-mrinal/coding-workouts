class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) # 5
        left = 0
        right = n - 1

        def condition(mid): # dupicate index
            count = sum([num <= mid for num in nums])
            return count > mid

        while left < right:
            mid = left + (right - left) // 2

            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
