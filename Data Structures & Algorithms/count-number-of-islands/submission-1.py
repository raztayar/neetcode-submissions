class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i not in range(m) or j not in range(n):
                return
            
            if grid[i][j] == "0" or (i, j) in visited:
                return
            
            visited.add((i,j))
            
            dir = [(1,0), (0,1), (-1,0), (0,-1)]

            for dr, dc in dir:
                nr, nc = i + dr, j + dc
                dfs(nr, nc)
            
            
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        
        return islands