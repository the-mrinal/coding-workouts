class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        st = deque([[0]])
        
        res = []
        # seen = set([0])
        
        while st:
            curr = st.popleft()
            
            index = curr[-1]
            
            if index == len(graph) -1:
                res.append(curr.copy())
                continue
            
            for n in graph[index]:
                st.append(curr + [n])
        
        return res