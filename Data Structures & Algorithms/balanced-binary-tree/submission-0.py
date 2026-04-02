# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def getHeight(root):
            if not root: return 0
            nonlocal res
            Lh = getHeight(root.left)
            Rh = getHeight(root.right)
            if abs(Lh-Rh) > 1:
                res = False
            return 1 + max(Lh, Rh)

        getHeight(root)
        return res