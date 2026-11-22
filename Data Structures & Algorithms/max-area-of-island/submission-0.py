class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        curr_max = 0
        visited = set()
        m, n = len(grid), len(grid[0])

        def bfs(i, j):
            Q = deque([(i, j)])
            dirs = ((1,0), (0,1), (-1,0), (0,-1))
            curr_area = 1

            while Q:
                (r, c) = Q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr in range(m) and nc in range(n) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        curr_area += 1
                        Q.append((nr, nc))
                
            return curr_area
                

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    area = bfs(i, j)
                    curr_max = max(area, curr_max)
        
        return curr_max
        
