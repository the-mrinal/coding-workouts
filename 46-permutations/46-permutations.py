class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def backtrack(st,end):
            if st == end:
                ans.append(nums[:])
            for i in range(st,end):
                nums[st],nums[i] = nums[i],nums[st]

                backtrack(st + 1,end)

                nums[st],nums[i] = nums[i], nums[st]


        backtrack(0,len(nums))
        
        return ans