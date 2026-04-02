class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c, distance):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == -1 or grid[r][c] < distance:
                return

            grid[r][c] = distance
            distance += 1
            for dr, dc in directions:
                dfs(r + dr, c + dc, distance)
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dfs(r, c, 0)