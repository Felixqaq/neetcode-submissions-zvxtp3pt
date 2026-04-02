import json
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return "[]"
        res = []
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res.append(None)

        while res and res[-1] == None:
            res.pop()

        return json.dumps(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "[]": return None
        data = json.loads(data)
        q = deque()
        i = 0
        head = TreeNode(data[i])
        q.append(head)
        i += 1
        while q:
            node = q.popleft()

            if i < len(data) and data[i] is not None:
                node.left = TreeNode(data[i])
                q.append(node.left)
            i += 1

            if i < len(data) and data[i] is not None:
                node.right = TreeNode(data[i])
                q.append(node.right)
            i += 1
        return head
