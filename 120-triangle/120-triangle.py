# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         directions = [[1,0],[1,1]]
#         size = len(triangle)
#         def dfs():
#             min_cost = float('inf')
#             stack = [[0,0,1,triangle[0][0]]]
#             while stack:
#                 x,y,level,cost = stack.pop()
#                 if level == size:
#                     print(cost)
#                     min_cost = min(min_cost,cost)
#                 else:
#                     for n_x,n_y in directions:
#                         a = n_x + x
#                         b = n_y + y
#                         # print(a,b,'---',level,size)
#                         if a < 0 or b < 0 or a >= size or b >= level+1:
#                             continue
#                         stack.append([a,b,level + 1,cost + triangle[a][b]])
#             return min_cost
#         return dfs()

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        curr = [0]*(n-1)
        prev = triangle[n-1]
        for level in range(n-2,-1,-1):
            # print(curr)
            for i in range(level + 1):
                curr[i] = triangle[level][i]+min(prev[i],prev[i+1])
            curr,prev = [0]*(level),curr
        return prev[0]