"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        ma = {}
        head = Node(node.val)
        ma[head.val] = head
        stack = [node]
        while stack:   
            cur = stack.pop()
            for neighbor in cur.neighbors:
                if neighbor.val not in ma:
                    ma[neighbor.val] = Node(neighbor.val)
                    stack.append(neighbor)
                ma[cur.val].neighbors.append(ma[neighbor.val])    
                
                    
        return ma[node.val]