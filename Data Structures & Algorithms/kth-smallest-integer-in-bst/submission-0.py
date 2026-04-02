# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = -1
        def dfs(root, k):
            if not root: return
            nonlocal count
            nonlocal ans
            dfs(root.left, k)
            print("count", count, "root.val", root.val)
            count += 1
            if count == k:
                ans = root.val
            dfs(root.right, k)
        
        dfs(root, k)
        return ans
