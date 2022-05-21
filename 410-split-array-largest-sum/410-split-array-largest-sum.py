class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
				# def isFeasible(thresold):
				# count = 1
				# total = 0
				# for num in nums:
				#        total += num
				# 			 if total > thres:
				# 								 total = num
				# 								 count += 1
				# 								 if count >  thres:
				# 											 return False
				# 	return True
        def feasible(thres):
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > thres:
                    total = num
                    count += 1
                    if count > m:
                        return False
            return True
        
        left = max(nums)
        right = sum(nums)
        
        while left < right:
            mid = left + (right - left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
                