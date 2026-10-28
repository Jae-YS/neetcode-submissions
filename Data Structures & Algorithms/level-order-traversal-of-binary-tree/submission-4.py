# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:      
        if not root:
            return []

        retVal = []
        queue = deque([root])  

        while queue:
            vals = []
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                vals.append(node.val) 
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            retVal.append(vals)

        return retVal
