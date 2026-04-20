class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        iset, jset = set(), set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    iset.add(i)
                    jset.add(j)

        for i in range(n):
            for j in range(m):
                if i in iset or j in jset:
                    matrix[i][j] = 0