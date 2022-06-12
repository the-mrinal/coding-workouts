
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
	
        maxScore = float('-inf')
        # [4,2,4,5,6]
        n = len(nums) # 5
        start = 0 

        visited = {}
        window_sum = 0
        maxSoFar = 0
        for end in range(0,n):
            window_sum += nums[end] # 4 6 10 11,17

            if nums[end] in visited:# yes 4 is visited
                prev = start # 0
                start = visited[nums[end]] + 1 # 1 
                while prev < start:
                    window_sum -= nums[prev] # 6
                    del visited[nums[prev]]
                    prev += 1


            visited[nums[end]] = end #{4:2,2:1,5:3,6:4 }
            maxSoFar = max(maxSoFar,window_sum) # 4,6,No change,11,17

        return maxSoFar
