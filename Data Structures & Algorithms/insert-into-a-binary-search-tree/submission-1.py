# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        temp = root
        while temp:
            if val >temp.val:
                if not temp.right:
                    temp.right = TreeNode(val)
                    break
                temp=temp.right
            else:
                if not temp.left:
                    temp.left=TreeNode(val)
                    break
                temp=temp.left
        return root
