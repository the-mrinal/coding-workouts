class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = {i:0 for i in range(numCourses)}
        adjMap = {i:[] for i in range(numCourses)}
        
        # 0 -> 1
        # 0 -> 1 and 1 > 0
        
        for main,pre in prerequisites:
            adjMap[pre].append(main)
            indeg[main] += 1
    
        res = []
        que = deque()
        for key,val in indeg.items():
            if val == 0:
                que.append(key)
  
        while que:
            curr = que.popleft()
            
            res.append(curr)
            
            for neigh in adjMap[curr]:
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    que.append(neigh)
        
        return True if len(res) == numCourses else False