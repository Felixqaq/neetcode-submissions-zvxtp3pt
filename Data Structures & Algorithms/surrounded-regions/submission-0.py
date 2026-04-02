class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        lives = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or board[r][c] == "X" or (r, c) in lives:
                return
            lives.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in lives:
                    board[r][c] = "X"
      