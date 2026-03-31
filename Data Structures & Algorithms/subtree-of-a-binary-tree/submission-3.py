# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subNode = None
        def findSubRoot(node):
            nonlocal subNode
            if not node:
                return 
            if node.val == subRoot.val:
                subNode = node
                return
            findSubRoot(node.left)
            findSubRoot(node.right)
        
        def equateTree(node1, node2):
            nonlocal subNode
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return (equateTree(node1.left, node2.left) and equateTree(node1.right, node2.right))
        findSubRoot(root)
        while True:
            if not subNode:
                return False
            if equateTree(subNode,subRoot):
                return True
            prev =subNode
            findSubRoot(subNode.left)
            findSubRoot(subNode.right)
            if prev == subNode:
                return False
    
            
        