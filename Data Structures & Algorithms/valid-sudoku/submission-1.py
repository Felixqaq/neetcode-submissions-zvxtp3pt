class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            cache = set()

            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in cache:
                    return False    
                
                cache.add(board[i][j])
            
        for i in range(9):
            cache = set()
            
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in cache:
                    return False    
                
                cache.add(board[j][i])
        index = [0, 3, 6]
        for ini in index:
            for inj in index:
                cache = set()
                for i in range(3):
                    for j in range(3):
                        if board[ini+i][inj+j] == '.':
                            continue
                        if board[ini+i][inj+j] in cache:
                            return False    
                        
                        cache.add(board[ini+i][inj+j])
        return True