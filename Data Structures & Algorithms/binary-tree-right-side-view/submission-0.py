# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        retVal = [] 
        while queue:
            n = len(queue)
            added = False
            for _ in range(n):
                node = queue.popleft()
                if not added:
                    retVal.append(node.val)
                    added = True
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)



        return retVal
        