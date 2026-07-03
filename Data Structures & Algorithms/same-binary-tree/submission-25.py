# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None and q or q is None and p:
            return False
        if p.val != q.val:
            return False
        
        if p.left and q.left:
            val = self.isSameTree(p.left, q.left)
            if not val:
                return False
        elif p.left and q.left is None or p.left is None and q.left:
            return False

        if p.right and q.right:
            val = self.isSameTree(p.right, q.right)
            if not val:
                return False
        elif p.right and q.right is None or p.right is None and q.right:
            return False

        return True