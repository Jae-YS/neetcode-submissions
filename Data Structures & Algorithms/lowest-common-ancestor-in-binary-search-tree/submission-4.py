# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def find_start(root, p, q):
            if root.left and root.val == q.val or root.right and root.val == p.val:
                return root
            if root.val > p.val and root.val < q.val:
                return root
            elif root.val < p.val:
                return find_start(root.right, p, q)
            elif root.val > q.val:
                return find_start(root.left, p, q)
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        return find_start(root, p, q)