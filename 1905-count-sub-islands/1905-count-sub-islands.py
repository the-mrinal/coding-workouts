class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

            m1 = len(grid1)
            n1 = len(grid1[0])

            m2 = len(grid2)
            n2 = len(grid2[0])

            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            islandstorem = set()
            for i in range(m1):
                for j in range(n1):
                    if grid1[i][j] == 1:
                        islandstorem.add((i,j))


            def dfs(x,y):
                st = [(x,y)]

                isSubIsland = True

                visited = set()

                while st:
                    c_x,c_y = st.pop()



                    if (c_x,c_y) not in islandstorem:
                        isSubIsland = False
                    grid2[c_x][c_y] = 0
                    for n_x,n_y in directions:
                        u_x = n_x + c_x
                        u_y = n_y + c_y
                        if u_x < 0 or u_x >= m2 or u_y < 0 or u_y >= n2 or grid2[u_x][u_y] == 0 or (u_x,u_y) in visited:
                            continue

                        st.append((u_x,u_y))
                        visited.add((u_x,u_y))

                return isSubIsland

            count = 0
            for i in range(m2):
                for j in range(n2):
                    if grid2[i][j] == 1:
                        if dfs(i,j):
                            count += 1

            return count
