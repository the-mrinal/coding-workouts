class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        horizontalCuts.append(h)
        verticalCuts.append(w)

        horizontalCuts = [0] + horizontalCuts
        verticalCuts = [0] + verticalCuts
        MOD = (10**9 + 7)
        maxHeight = float('-inf')
        for i in range(1,len(horizontalCuts)):
            maxHeight = max(maxHeight,horizontalCuts[i] - horizontalCuts[i-1])
        
        maxWidth = float('-inf')
        for j in range(1,len(verticalCuts)):
            maxWidth = max(maxWidth,verticalCuts[j] - verticalCuts[j-1])
            
        maxSize = maxHeight * maxWidth
        return maxSize%MOD
