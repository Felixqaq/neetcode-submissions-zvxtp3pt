"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        visited = {}

        def dfs(node):
            if node.val not in visited:
                visited[node.val] = Node(node.val)
            else: 
                return visited[node.val]
            newNeighbors = []
            for n in node.neighbors:
                newNeighbors.append(dfs(n))
            visited[node.val].neighbors = newNeighbors
            return visited[node.val]
        return dfs(node)