class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)

        if nums[right - 1] < target:
            return right

        def condition(mid):
            if nums[mid] >= target:
                return True
            return False

        while left < right:
            mid = left + (right - left)//2

            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left 
