# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        res = 0
        def dfs(root, maxN):
            if not root: return 0
            temp = 0
            if root.val >= maxN:
                maxN = root.val
                temp += 1
            return temp + dfs(root.left, maxN) + dfs(root.right, maxN)
        res = dfs(root, root.val-1)
        return res