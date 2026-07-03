# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root and val > root.val:
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                node = TreeNode(val=val)
                root.right = node                
                return root
        elif root and val < root.val:
            if root.left:
                self.insertIntoBST(root.left, val)
            else:                
                node = TreeNode(val=val) 
                root.left = node
                return root
        else:
            node = TreeNode(val=val) 
            return node
        return root