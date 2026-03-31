# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def preOrder(p_temp, q_temp):
            if not p_temp and not q_temp:
                return True
            if not p_temp or not q_temp:
                return False
            if p_temp.val != q_temp.val:
                return False
            return (preOrder(p_temp.left, q_temp.left) and preOrder(p_temp.right, q_temp.right))
        return preOrder(p,q)


        