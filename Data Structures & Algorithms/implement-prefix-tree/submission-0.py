class TreeNode:
    def __init__(self):
        self.child = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not c in cur.child:
                cur.child[c] = TreeNode()
            cur = cur.child[c]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if not c in cur.child:
                return False
            cur = cur.child[c]
        if cur.end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if not c in cur.child:
                return False
            cur = cur.child[c]
        return True
        