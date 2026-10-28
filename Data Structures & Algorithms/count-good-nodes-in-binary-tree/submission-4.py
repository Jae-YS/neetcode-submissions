# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(cur_max, node): 
            if node is None:
                return 0
            cur_max = max(cur_max, node.val)
            add = 1 if node.val >= cur_max else 0    
            return dfs(cur_max, node.right) + dfs(cur_max, node.left) + add
        
        
        
        return dfs(float('-inf'), root)
            
            
            