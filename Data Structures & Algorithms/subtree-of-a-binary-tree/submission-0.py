# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        def checkSame(root: Optional[TreeNode], subRoot: Optional[TreeNode]):
            if not subRoot and not root: return True
            if not subRoot or not root: return False
            if root.val != subRoot.val:
                return False

            return checkSame(root.left, subRoot.left) and checkSame(root.right, subRoot.right)


        res = checkSame(root, subRoot)

        return res or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)