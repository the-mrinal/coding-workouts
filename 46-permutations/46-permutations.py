class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def permutationHelper(index):
            nonlocal n
            if index == n - 1:
                return [[nums[index]]]
            
            perm = permutationHelper(index + 1)
            new_perm = []
            
            for i in range(len(perm)):
                for j in range(len(perm[i])+1):
                    curr_p = perm[i][:j] + [nums[index]] + perm[i][j:]
                    new_perm.append(curr_p)
            return new_perm
        return permutationHelper(0)