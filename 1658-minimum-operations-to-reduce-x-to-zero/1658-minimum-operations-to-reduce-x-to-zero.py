class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        hashMap = {}
        n = len(nums)
        if n == 1:
            return 1 if nums[0] == x else -1
        
        sums = 0
        for i in range(n):
            hashMap[sums] = i
            sums += nums[i]
        sums = 0
        res = float('inf')
        for j in range(n-1,-1,-1):
            target = x - sums
            if target in hashMap and hashMap[target] <= j + 1:
                res = min(res,n-1-j+hashMap[target])
            
            sums += nums[j]
        
        return res if res < float('inf') else -1
                