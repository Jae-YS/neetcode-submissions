# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return False

        heap = []
        stack = [root]

        while stack:
            node = stack.pop()
            heapq.heappush(heap, -node.val)
            if len(heap) > k:
                heapq.heappop(heap)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)



        return -heap[0]
        