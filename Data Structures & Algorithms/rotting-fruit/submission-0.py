class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Q = deque()
        curr_minute = 0
        dirs = ((1,0), (0,1), (-1,0), (0,-1))

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    Q.append((i, j, 0))
        

        while Q:
            r, c, minute = Q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr in range(m) and nc in range(n) and grid[nr][nc] == 1:
                    curr_minute = minute + 1
                    grid[nr][nc] = 2
                    print(f"{nr},{nc} turned rotten")
                    Q.append((nr, nc, curr_minute))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return curr_minute


