# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        store = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            store.append(node)
            inorder(node.right)
        inorder(root)
        node1,node2 = None,None
        for i in range(len(store)-1):
            if store[i].val > store[i+1].val:
                node2 = store[i+1]
                if node1 is None:
                    node1 = store[i]
                else:
                    break
        node1.val, node2.val = node2.val, node1.val




        