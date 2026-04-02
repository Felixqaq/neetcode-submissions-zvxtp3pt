class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(i, j, wordi):
            if wordi == len(word):
                return True
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return False

            if (i, j) in path:
                return False

            if not(wordi < len(word) and board[i][j] == word[wordi]):
                return False

            path.add((i, j))
            wordi += 1
            res = (dfs(i+1, j, wordi) or
                    dfs(i-1, j, wordi) or
                    dfs(i, j+1, wordi) or
                    dfs(i, j-1, wordi))

            path.remove((i, j))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                self.wordi = 0
                if dfs(r, c, 0): return True

        return False
