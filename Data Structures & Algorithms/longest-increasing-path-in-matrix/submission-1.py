class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        arrive = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(i, j):
            if i not in range(len(matrix)) or j not in range(len(matrix[0])):
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]

            beadd = 0
            for ini, inj in directions:
                if i + ini in range(len(matrix)) and j + inj in range(len(matrix[0])):
                    if matrix[i][j] > matrix[i + ini][j + inj]:
                        beadd = max(beadd, dfs(i + ini, j + inj))
            dp[(i, j)] = 1 + beadd
            return dp[(i, j)]

            
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i, j))
        return res