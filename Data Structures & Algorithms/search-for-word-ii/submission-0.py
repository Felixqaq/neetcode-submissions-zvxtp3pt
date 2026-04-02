class TreeNode:
    def __init__(self):
        self.child = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if not c in cur.child:
                cur.child[c] = TreeNode()
            cur = cur.child[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TreeNode()
        for word in words:
            root.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        res = set()
        visited = set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] not in node.child or (r, c) in visited):
                return 
            visited.add((r, c))
            node = node.child[board[r][c]]
            word += board[r][c]

            if node.isWord:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
