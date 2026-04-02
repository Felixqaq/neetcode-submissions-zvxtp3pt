class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        it = 0
        while fresh > 0 and q:
            q_len = len(q)
            for _ in range(q_len):
                r, c = q.popleft()
                for dr, dc in directions:
                    if r + dr in range(0, rows) and c + dc in range(0, cols) and grid[r + dr][c + dc] == 1:
                        fresh -= 1
                        grid[r + dr][c + dc] = 2
                        q.append((r + dr, c + dc))
            it += 1

        if fresh != 0:
            return -1
        return it