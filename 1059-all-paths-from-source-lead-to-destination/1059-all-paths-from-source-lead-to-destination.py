

# class Solution:
#     def leadsToDestination(self, n: int, edges: List[List[int]], src: int, dest: int) -> bool:

#             adjMap = defaultdict(list)

#             for start,end in edges:
#                 adjMap[start].append(end)

#             visited = set()
            
#             def dfs(v):
#                 if v in visited:
#                     return False
                
#                 if not adjMap[v]:
#                     return v == dest
                
#                 visited.add(v)
#                 for neigh in adjMap[v]:
#                     if not dfs(neigh):
#                         return False
                
#                 visited.remove(v)
#                 return True
            
#             return dfs(src)

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], src: int, dest: int) -> bool:

            adjMap = defaultdict(set)

            for start,end in edges:
                adjMap[start].add(end)

            st = [(src,[src])]

            while st:
                v,path = st.pop(-1)

                if v not in adjMap:
                    if v != dest:
                        print('dffe',v,dest)
                        return False
                    else:
                        continue

                for neigh in adjMap[v]:
                    if neigh in path:
                        print('fe')
                        return False
                    else:
                        st.append((neigh,path + [neigh]))

            return True
            
        
        
        
        
        