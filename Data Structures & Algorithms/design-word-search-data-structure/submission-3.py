class Node:
    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not c in cur.child:
                cur.child[c] = Node()
            cur = cur.child[c]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for children in cur.child.values():
                        if dfs(i + 1, children):
                            return True
                    return False
                else:
                    if not c in cur.child:
                        return False
                    cur = cur.child[c]
            return cur.end
        
        return dfs(0, self.root)
    
