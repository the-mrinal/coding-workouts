class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        src = 0
        dest = len(graph) - 1
        
        que = deque([[src,[src]]])


        ans = []
        

        while que:
            curr,path = que.popleft()

            if curr == dest:
                ans.append(path.copy())
                continue
            for b in graph[curr]:
                que.append([b,path + [b]])
        return ans