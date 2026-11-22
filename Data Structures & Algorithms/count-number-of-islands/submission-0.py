class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        m, n = len(grid), len(grid[0])

        def bfs(i, j):
            Q = deque([(i, j)])

            while Q:
                r, c = Q.popleft()
                dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr in range(m) and nc in range(n) and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        Q.append((nr, nc))
            



        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == "1":
                    visited.add((i,j))
                    islands += 1
                    bfs(i, j)
        
        return islands