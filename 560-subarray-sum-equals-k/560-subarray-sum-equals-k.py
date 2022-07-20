class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = defaultdict(int)
        currSum = 0
        count = 0
        for num in nums:
            currSum += num
            
            if currSum == k:
                count += 1
            
            count += hashMap[currSum - k]
            
            hashMap[currSum] += 1
            
        return count