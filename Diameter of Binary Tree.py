# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if (root is None):
            return 0
        
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        
        ldia = self.diameterOfBinaryTree(root.left)
        rdia = self.diameterOfBinaryTree(root.right)
        
        return max(lheight+rheight,max(ldia,rdia))
    
    def height(self,root):
        if (root is None):
            return 0
        else:
            return 1 + max(self.height(root.left),self.height(root.right))
        
