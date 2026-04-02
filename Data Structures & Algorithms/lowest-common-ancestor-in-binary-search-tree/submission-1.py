# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: return None
        ans = None

        def dfs(root, p, q):
            if not root: return False
            nonlocal ans
            l = dfs(root.left, p, q)
            r = dfs(root.right, p, q)
            mid = root.val == q.val or root.val == p.val
            if l + r + mid >= 2:
                ans = root
            return l or r or mid

        dfs(root, p, q)
        return ans