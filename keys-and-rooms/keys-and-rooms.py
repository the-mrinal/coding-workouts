class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        que = deque([])
        que.append(0)
        visited.add(0)
        while que:
            curr = que.popleft()

            for room in rooms[curr]:
                if room not in visited:
                    que.append(room)
                    visited.add(room)
        
        if len(visited) == len(rooms):
            return True
        return False