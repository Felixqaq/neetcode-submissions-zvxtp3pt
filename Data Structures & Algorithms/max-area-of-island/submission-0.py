class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.count = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return 
            grid[r][c] = 0
            
            self.count += 1
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return 

        for r in range(rows):
            for c in range(cols):
                dfs(r, c)
                res = max(res, self.count)
                self.count = 0

        return res