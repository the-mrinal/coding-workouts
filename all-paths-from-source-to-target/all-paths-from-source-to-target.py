class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        stack = [[0,[0]]]
        n = len(graph)
        res = []
        while stack:
            curr,path = stack.pop()
            if curr == n - 1:
                res.append(path.copy())
                continue

            for neigh in graph[curr]:
                stack.append([neigh,path + [neigh]])

        return res
