# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pq = deque()
        qp = deque()

        if p is None and q is None:
            return True

        if p is None or q is None:
            return False
        


        pq.append(p)
        qp.append(q)

        while pq or qp:
            
            n = len(pq)
            for _ in range(n):
                p1 = pq.popleft()
                q1 = qp.popleft()  
                if q1.val != p1.val:
                    return False
                
                if p1.right and not q1.right or q1.right and not p1.right:
                    return False
                
                if q1.left and not p1.left or p1.left and not q1.left:
                    return False
            
                if p1.right:
                    pq.append(p1.right)
                    qp.append(q1.right)

                if p1.left:
                    pq.append(p1.left)
                    qp.append(q1.left)

        return True