# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.maxN = root.val
        def dfs(root):  
            if not root:return 0
            left  = dfs(root.left)
            right = dfs(root.right)
            leftM = max(left, 0)
            rightM = max(right, 0)
            self.maxN = max(self.maxN, root.val+leftM+rightM)

            
            
            return root.val + max(leftM, rightM)
        dfs(root)
        return self.maxN
