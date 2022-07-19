class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        
        stack = []
        for start,end in intervals:
            if stack:
                prev_start = stack[-1][0]
                prev_end = stack[-1][1]
                
                if start <= prev_end:
                    stack.pop()
                    new_start = min(start,prev_start)
                    new_end = max(end,prev_end)
                    stack.append((new_start,new_end))
                else:
                    stack.append((start,end))
            else:
                stack.append((start,end))
        return stack