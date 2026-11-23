class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))

        Q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    Q.append((i, j))
                    visited.add((i, j))

        while Q:
            r, c = Q.popleft()
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr in range(m) and nc in range(n) and (nr, nc) not in visited and grid[nr][nc] != -1:
                    grid[nr][nc] = grid[r][c] + 1
                    visited.add((nr, nc))
                    Q.append((nr, nc))
