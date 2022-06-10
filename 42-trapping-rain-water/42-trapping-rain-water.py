class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0]*n
        maxRight = [0]*n
        ri = n - 2
        for li in range(1,n):
            if height[li - 1] > maxLeft[li-1]:
                maxLeft[li] = height[li - 1]
            else:
                maxLeft[li] = maxLeft[li - 1]
            if height[ri + 1] > maxRight[ri + 1]:
                maxRight[ri] = height[ri + 1]
            else:
                maxRight[ri] = maxRight[ri + 1]
            ri -= 1
            
        print(maxLeft)
        print(maxRight)
        waterLogged = 0
        for i in range(n):
            local_min = min(maxLeft[i],maxRight[i])
            waterLogged +=(local_min - height[i] if height[i] < local_min else 0)
        
        return waterLogged