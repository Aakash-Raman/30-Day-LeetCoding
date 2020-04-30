# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        i = 0
        l = len(arr)
        return self.pathfinder(root, arr, i, l)
    def pathfinder(self, root, arr, i, l):
        if(root is None):
            return l == 0
        if(i == l-1 and (root.val == arr[i]) and (root.left == None and root.right == None)):
            return True
        if(i < l and (root.val == arr[i])):
            return (self.pathfinder(root.left, arr, i + 1, l) or self.pathfinder(root.right, arr, i + 1, l))
