class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        
        def dfs():
            stack = [0]
            visited = set()
            visited.add(0)
            count = n
            while stack:
                curr = stack.pop()
                count -= 1
                if count == 0:
                    return True
                
                for neigh in rooms[curr]:
                    if neigh not in visited:
                        stack.append(neigh)
                        visited.add(neigh)
            return False
        return dfs()