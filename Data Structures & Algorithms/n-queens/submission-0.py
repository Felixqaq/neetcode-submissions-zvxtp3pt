class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:return [["Q"]]
        board = [ '.' * n for _ in range(n)]
        res = []
        def check(i, j):
            if i > n:
                return False
            if j > n:
                return False
            ti = i - 1
            while ti >= 0:
                if board[ti][j] == 'Q':
                    return False
                ti -= 1
            tj = j - 1
            ti = i - 1

            while ti >= 0 and tj >= 0:
                if board[ti][tj] == 'Q':
                    return False
                ti -= 1
                tj -= 1
            ti = i - 1
            tj = j + 1

            while ti >= 0 and tj < n:
                if board[ti][tj] == 'Q':
                    return False
                ti -= 1
                tj += 1

            return True
         
        def bfs(i):
            if i == n:
                res.append(board.copy())
                return

            for j in range(n):
                if check(i, j):
                    board[i] = board[i][:j] + 'Q' + board[i][j + 1:]
                    print(board)
                    bfs(i + 1) 
                    board[i] = board[i][:j] + '.' + board[i][j + 1:]
        bfs(0)
        return res