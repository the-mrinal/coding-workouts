class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = {i:0 for i in range(numCourses)}
        adjMap = {i:[] for i in range(numCourses)}
        
        for a,b in prerequisites:
            adjMap[b].append(a)
            indeg[a] += 1
        
        que = deque()
        
        for key,val in indeg.items():
            if val == 0:
                que.append(key)
                
                
        res = []
        while que:
            curr = que.popleft()
            
            res.append(curr)
            
            for child in adjMap[curr]:
                indeg[child] -= 1
                if indeg[child] == 0:
                    que.append(child)
        
        return res if len(res) == numCourses else []