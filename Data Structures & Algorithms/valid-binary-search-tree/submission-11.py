# Definition for a binary tree node.   
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, ub, lb):
            if not root:
                return True
            if root.val >= ub or root.val <= lb:
                return False
            
            if root.right and root.right.val <= root.val or root.left and root.left.val >= root.val:
                return False
            
            return check(root.right, ub, root.val) and check(root.left, root.val, lb)
        


        if root.right and root.right.val <= root.val or root.left and root.left.val >= root.val:
            return False
        
        return check(root.right, float('inf'), root.val) and check(root.left, root.val, float('-inf'))