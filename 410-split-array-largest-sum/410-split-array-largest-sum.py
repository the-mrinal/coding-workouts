class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)
        n = len(nums)
        def condition(maxSum):
            totalN,count = 0,1
            for i in range(n):
                totalN += nums[i]
                if totalN > maxSum:
                    totalN = nums[i]
                    count += 1
                if count > m:
                    return False
            return True

        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left