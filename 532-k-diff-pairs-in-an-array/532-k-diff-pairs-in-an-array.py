class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = 0
        counter = Counter(nums)
        
        for x in counter:
            if k > 0 and x +k in counter:
                result += 1
            elif k == 0 and counter[x] > 1:
                result += 1
        
        return result