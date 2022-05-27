class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        res = [0 for _ in range(n)]
        
        stack = []
        stack.append([temp[0],0])
        
        for i in range(1,n):
            if stack[-1][0] < temp[i]:
                while stack and stack[-1][0] < temp[i]:
                    val,index = stack[-1]
                    stack.pop()
                    res[index] = i - index
            stack.append([temp[i],i])
            
        
        return res