# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.findleaf(root1) == self.findleaf(root2)
        
    def findleaf(self, root):
        if not root:
            return []
        if not (root.left or root.right):
            return [root.val]
        return self.findleaf(root.left) + self.findleaf(root.right)