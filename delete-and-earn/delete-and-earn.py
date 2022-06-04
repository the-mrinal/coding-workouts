# limit = 10^4 ie, 10001

# points = [0] * 10001
# for num in nums:
# points[num] += num
# def dp(i):
# 	if i == 1:
# 		return points[i]
# 	if i == 2:
# 		return max(points[0],points[1])

# 	point = max(dp(i-1),dp(i-2)+points[i])

# 	return points


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        points = [0] * 10001
        for num in nums:
            points[num] += num
    
        def dp(i):
            if i == 0:
                return points[0]
            if i == 1:
                return max(points[0],points[1])

            if i not in memo:
                t = dp(i-1)
                t1 = dp(i-2)+points[i]
        
                p = max(t,t1)
                memo[i] = p

            return memo[i]
        
        memo = {}
        return dp(max(nums))
