class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ROW, COL = len(s), len(t)
        dp = [[False for _ in range(COL)] for _ in range(ROW)]
        for i in range(ROW):
            for j in range(COL):
                if s[i] == t[j]:
                    dp[i][j] = True
                    
        def dfs(i, cur_j):
            if i >= COL:
                return 1
            if cur_j >= ROW:
                return 0
            res = 0
            for j in range(cur_j, ROW):
                if dp[j][i]:
                    res += dfs(i+1, j+1)
            return res

        return dfs(0, 0)