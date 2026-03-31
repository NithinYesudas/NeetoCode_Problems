# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inOrder = []
        def inOrderHelper(node):
            if not node:
                return
            inOrderHelper(node.left)
            inOrder.append(node.val)
            inOrderHelper(node.right)
        inOrderHelper(root)
        for i in range(1,len(inOrder)):
            if inOrder[i]<=inOrder[i-1]:
                return False
        return True
            
        