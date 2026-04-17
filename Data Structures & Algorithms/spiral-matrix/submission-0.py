class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return [matrix[0][0]]
        total = len(matrix) * len(matrix[0])
        direct = 0
        move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        edge = [[0, len(matrix[0])], [len(matrix), len(matrix[0])-1], [len(matrix)-1, -1], [0, 0]]
        print(edge)
        edgeMove = [[1, -1], [-1, -1], [-1, 1], [1, 1]]
        res = []
        i, j = 0, 0

        while total:
            print(i, j)
            res.append(matrix[i][j])
            total -= 1
            i += move[direct][0]
            j += move[direct][1]
            if [i, j] == edge[direct]:
                i -= move[direct][0]
                j -= move[direct][1]
                
                edge[direct][0] += edgeMove[direct][0]
                edge[direct][1] += edgeMove[direct][1]

                if direct != 3:
                    direct += 1
                else:
                    direct = 0
                
                i += move[direct][0]
                j += move[direct][1]
            
        return res